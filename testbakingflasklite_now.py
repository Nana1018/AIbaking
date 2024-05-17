
#Tensorflow package
#import pandas as pd
import numpy as np
# import os

# import tensorflow as tf
# from tensorflow.keras.models import load_model
# os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'
#Usage:Train send warning: response = requests.get("http://127.0.0.1:5050/")
# a01_flask_server.py
#Using tflite to reduce the size
import tflite_runtime.interpreter as tflite
#import tensorflow as tf
from flask import Flask
from flask import render_template, request

app = Flask(__name__)
# 
recipestr = ''
l = ''
BS = 32
labelname = ["Bread", "Cake", "Cookie", "Croissant"]
# df = pd.read_csv('bakingrecipe.csv')
# df.pop('Label')

#Loading model
#print("[INFO] Loading model...")
#baking_model = load_model("baking")
TFLITE_MODEL_PATH = 'bakingTt.tflite'
TFLITE_MODEL_PATH_recipe = 'bakindgen.tflite'

# Normalizing the data
def normalize(test_data):
    data_max = np.array([3, 745, 310, 6, 45, 310, 3, 2.5, 120, 180, 3, 400, 80, 575, 400, 4])
    data_min = np.array([0, 10, 0, 0, 0 , 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # print(data_max)
    # print(data_min)
    # print(test_data)
    return (test_data - data_min) /(data_max - data_min)

def recover(normal, index=None):
    data_max = np.array([3, 745, 310, 6, 45, 310, 3, 2.5, 120, 180, 3, 400, 80, 575, 400, 4])
    data_min = np.array([0, 10, 0, 0, 0 , 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    if isinstance(normal, list):
        recovered_values = []
        for i in range(len(normal)):
            recovered_values.append((data_max[i] - data_min[i]) * normal[i] + data_min[i])
        return recovered_values
    else:
        return (data_max[index] - data_min[index]) * normal + data_min[index]


# def recover(normal, index):
#     data_max = np.array([3, 745, 310, 6, 45, 310, 3, 2.5, 120, 180, 3, 400, 80, 575, 400, 4])
#     data_min = np.array([0, 10, 0, 0, 0 , 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     # print(data_max[index])
#     # print(data_min[index])        
#     return (data_max[index] - data_min[index]) * normal + data_min[index]

# dealing with data to make '' to zero
def datadeal(Yeast, Flour, Sugar, Egg, Oil, Milk, Soda, Powder, Almond, Chocolate, Banana, Flaky, Honey, Water, Butter, Salt):
    yeast = float(Yeast) if Yeast !='' else 0
    flour = float(Flour) if Flour !='' else 0
    sugar = float(Sugar) if Sugar !='' else 0
    egg = float(Egg) if Egg !='' else 0
    oil = float(Oil) if Oil !='' else 0
    milk = float(Milk) if Milk !='' else 0
    soda = float(Soda) if Soda !='' else 0
    powder = float(Powder) if Powder !='' else 0
    almond = float(Almond) if Almond !='' else 0
    chocolate = float(Chocolate) if Chocolate !='' else 0
    banana = float(Banana) if Banana !='' else 0
    flaky = float(Flaky) if Flaky !='' else 0
    honey = float(Honey) if Honey !='' else 0
    water = float(Water) if Water !='' else 0
    butter = float(Butter) if Butter !='' else 0
    salt = float(Salt) if Salt !='' else 0

    dessert = [[yeast, flour, sugar, egg, oil, milk, soda, powder, almond, chocolate, banana, flaky, honey, water, butter, salt]]

    return dessert

# Predicting the results from tflite.interpreter
def predictlite(testX):
    testX=np.array(testX, dtype=np.float32)
    interpreter = tflite.Interpreter(model_path=TFLITE_MODEL_PATH)
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Test the model on random input data.
    interpreter.set_tensor(input_details[0]['index'], testX)

    interpreter.invoke()

    predictions = interpreter.get_tensor(output_details[0]['index'])
    direction = interpreter.get_tensor(output_details[1]['index'])
    
    print('***************')
    print(predictions[0])
    print('***************')
    print(direction[0])

    return predictions[0], direction[0]


# Predicting the dessert for the recipe
def predictions(testdata):

    testX = np.array(testdata)

    if testX.sum() != 0 and testX[0, 1] != 0 and testX[0, 2] != 0:

        testX = normalize(testX)

        testX = np.nan_to_num(testX)
        # print(testX)

        #predictions = baking_model.predict(testX)[0]


        # The function `get_tensor()` returns a copy of the tensor data.
        # Use `tensor()` in order to get a pointer to the tensor.
        predictions, direction = predictlite(testX)
        print(direction)
        tem= direction[0]
        print(tem)
        time = direction[1]
        T = np.round(recover(tem, -2))
        t = np.round(recover(time, -1))
        print(T)
        print(t)
        np.set_printoptions(precision=3, suppress=True)

        print(labelname)
        print("******************")
        print(predictions)
        print(tem)
        print(time)

        confidence = np.round(predictions[0]  * 100)
        T = int(np.round(T))
        t = int(np.round(t))

        confidence = np.round(predictions * 100)
        l = '預測為:' + labelname[np.argmax(confidence)]

        print(confidence)
    else:
        confidence = [0, 0 ,0 ,0]
        l = '麵粉和糖一定要輸入喔!'
    return(confidence, T, t, l)

def recipelite(recipestr):

    recipestr = np.array(recipestr, dtype=np.float32)
    interpreter = tflite.Interpreter(model_path=TFLITE_MODEL_PATH_recipe)
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Test the model on random input data.
    interpreter.set_tensor(input_details[0]['index'], recipestr)

    interpreter.invoke()

    recipe = interpreter.get_tensor(output_details[0]['index'])
    print("recipelite*************")
    print(recipe)

    return recipe[0]

def make1(Bread, Cake, Cookie, Croissant):
    #權愈變數
    #Preparint the class
    # interpreter = tflite.Interpreter(model_path=TFLITE_MODEL_PATH_recipe)
    # recipestr = ''
    b = float(Bread) /100if Bread !='' else 0
    print('Bread(%):',b)
    ca = float(Cake) /100 if Cake !='' else 0 
    print('Cake(%):',ca)
    co = float(Cookie) /100 if Cookie !='' else 0
    print('Cookie(%):',co)
    cr = float(Croissant) /100 if Croissant !='' else 0
    print('Croissant(%):',cr)

    taste = [[b, ca, co, cr]]
    print(taste)

    return taste

    # recipe = recipe_model.predict(taste)[0]
    # print(recipe)

def recipe1(taste):
    recipe = recipelite(taste)
    print("recipe1*************")
    print(recipe)
    R = np.round(recover(normal = recipe),1)[0]
    print(R)

    I = 'Yeast :' + str(R[0]) + 'g  '

    I = I + 'Flour : ' + str(R[1]) + 'g  '

    I = I + 'Sugar : ' + str(R[2]) + 'g  '
        
    I = I + 'Egg : ' + str(R[3]) + 'g  \n'
        
    I = I + 'Oil : ' + str(R[4]) + 'g  '
        
    I = I + 'Milk : ' + str(R[5]) + 'g  '

    I = I + 'Baking Soda : ' + str(R[6]) + '(tsp)  \n'

    I = I + 'Baking Powder : ' + str(R[7]) + '(tsp)  '

    I = I + 'Almond P : ' + str(R[8]) + 'g \n '

    I = I + 'Chocolate P : ' + str(R[9]) + 'g  '

    I = I + 'Banana : ' + str(R[10]) + 'g  '

    I = I + 'Flaky Butter : ' + str(R[11]) + 'g \n '

    I = I + 'Honey : ' + str(R[12]) + 'g  '

    I = I + 'Water : ' + str(R[13]) + 'g  '

    I = I + 'Butter : ' + str(R[14]) + 'g  '

    I = I + 'Salt : ' + str(R[15]) + 'g  '


    recipe = '食譜為:' + I
    print(recipe)
    return recipe
            # print(recipestr)
    # Dlabel = tk.Label(root, font = ('Arial',14), text= recipestr, justify='left', bg ='#FCF8E8', fg='#574740')
    # Dlabel.place(x = column1, y=350)

@app.route("/")
def home():
    return render_template('indexbake.html')


@app.route("/baking", methods=['POST'])
def baking():
    #print('******baking******')
    #Getting the data from the form
    Yeast = request.form['Yeast'] 
    Flour = request.form['Flour']
    Sugar = request.form['Sugar']
    Egg = request.form['Egg']
    Oil = request.form['Oil']
    Milk = request.form['Milk']
    Soda = request.form['Soda']
    Powder = request.form['Powder']
    Almond = request.form['Almond']
    Chocolate = request.form['Chocolate']
    Banana = request.form['Banana']
    Flaky = request.form['Flaky']
    Honey = request.form['Honey']
    Water = request.form['Water']
    Butter = request.form['Butter']
    Salt = request.form['Salt']

    data = datadeal(Yeast, Flour, Sugar, Egg, Oil, Milk, Soda, Powder, Almond, Chocolate, Banana, Flaky, Honey, Water, Butter, Salt)

    confidence, T, t, l = predictions(data)
    print("*************")
    print(confidence)
    print(T)
    print(t)
    print(l)
    print(str(T))

    if np.max(confidence) == 50:
            first = np.argmax(confidence)
            second = np.argmax(confidence[np.argmax(confidence)+1:])+ np.argmax(confidence)+1
            # print(np.max())
            if first == 0 and second == 2:
                d = "/static/breakie.jpg"
            elif first == 1 and second == 2:
                d = "/static/cakie.jpg"
            elif first == 2 and second == 3:
                d = "/static/cruskie.jpg"

        elif np.argmax(confidence) == 0:
            d = "/static/bread.jpg"
        elif np.argmax(confidence) == 1:
            d = "/static/cake.jpg"
        elif np.argmax(confidence) == 2:
            d = "/static/cookie.jpg"
        elif np.argmax(confidence) == 3:
            d = "/static/croissant.jpg"
    
    return render_template('resultcr.html', bread= str(confidence[0]),
        cake = str(confidence[1]),
        cookie = str(confidence[2]),
        croissant = str(confidence[3]),
        Temperature = str(T),
        Time = str(t),
        message = l)
    

@app.route("/make")
def make():
        return render_template('indexmake.html')

@app.route("/making", methods=['POST'])
def making():
    Bread = request.form['Bread']
    Cake = request.form['Cake']
    Cookie = request.form['Cookie']
    Croissant = request.form['Croissant']

    make = make1(Bread, Cake, Cookie, Croissant)
    recipe = recipe1(make)

        
    return render_template('indexmake.html', message = recipe)   
        # return render_template('resultcr.html', bread= str(confidence[0]),
        # cake = str(confidence[1]),
        # cookie = str(confidence[2]),
        # croissant = str(confidence[3]),
        # message = l)



# return []

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5050)
