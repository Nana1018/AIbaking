# AI Michelin Dessert Master System 
## About:
This study utilizes neural network technology to establish a model for French dessert recipes. 
The system can identify dessert types from recipes. It empowers AI with innovative capabilities to create desserts with entirely new flavors, such as "Cakie" (50% cake, 50% cookie) and "Breakie" (50% bread, 50% cookie). 
Additionally, it provides baking guidelines for users, recommending appropriate oven temperatures and baking times. 
It can also generate dessert recipes based on taste preferences.

## How it Works
The system consists of two pages.
The first page is the AI Baking interface, and the other page is the Generate Recipe page.

##### AI baking interface: 
The recipe have 16 ingredients, enter the required ingredients and their weight (in grams) into the box grid. Press the "送出" button,the dessert and baking method of this recipe will be obtained through the category neural model and the baking method neural model.
You can also get the probability that the system recognizes that type of dessert.

##### Generate Recipe interface:
Pressing the "生成食譜" button will navigate to the Generate Recipe page. In this screen, you'll enter the desired taste preferences. Pressing the "生成" button will utilize the generation neural model to generate an ingredient recipe that matches the taste requirements for this dessert.

## Demo
https://nowbaking-my-team-fdf1b477.vercel.app/?

## File Description

#### Programs and Models.

          testbakingflasklite_now.py = Main program.
          bakingTt.tflite = the model used by AI baking.
          bakindgen.tflite = the model used by Generate Recipe.
     
#### Web App Program.

All in the tempaltes file.

          indexbake.html = the main webpage used for AI baking.
          resultcr.html = the internal webpage used for showing recipes.
          indexMake.html = the webpage used for Generating Recipe.
  
## Citing

@article{AI Baking,

Author={Anna. {Lo},

title={AI Michelin Dessert Master System - A Study on the Application of Artificial Intelligence in Dessert Making},

year={2024}
}
#### Project Leader
Lo, Hsin-Le
