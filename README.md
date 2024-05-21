[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)

# AI Michelin Dessert Master System 
## About:
This study utilizes neural network technology to establish a model for French dessert recipes. 
The system can identify dessert types from recipes. It empowers AI with innovative capabilities to create desserts with entirely new flavors, such as "Cakie" (50% cake, 50% cookie) and "Breakie" (50% bread, 50% cookie). 
Additionally, it provides baking guidelines for users, recommending appropriate oven temperatures and baking times. 
It can also generate dessert recipes based on taste preferences.

## Demo
https://nowbaking-my-team-fdf1b477.vercel.app/?

## How it Works
The system consists of two pages.
The first page is the AI Baking interface, and the other page is the Generate Recipe page.

AI baking interface: The recipe have 16 ingredients, enter the required ingredients and their weight (in grams) into the box grid.
Press the "送出" button to get the dessert and baking method corresponding to this recipe. You can also get the probability that the system recognizes that type of dessert.

Generate Recipe interface:Pressing the "生成食譜" button will navigate to the Generate Recipe page. In this screen, you'll enter the desired taste preferences. Pressing the "生成" button will utilize the generation neural model to create an ingredient recipe that matches the taste requirements for this dessert.

## File Description

Programs and Models.

          testbakingflasklite_now.py = Main program.
          bakingTt.tflite = Is the model used by AI baking.
          bakindgen.tflite = Is the model used by Generate Recipe.
     
Web App Program.

All in the tempaltes file.

          indexbake.html = Is the main webpage used for AI baking.
          resultcr.html = Is the internal webpage used for AI baking show recipe.
          indexMake.html = Is the webpage used for Generate Recipe.
  
## One-Click Deploy

@article{Lisa_My_awesome_research_2021,
  author = {Lisa, Mona and Bot, Hew},
  doi = {10.0000/00000},
  journal = {Journal Title},
  month = {9},
  number = {1},
  pages = {1--10},
  title = {{My awesome research software}},
  volume = {1},
  year = {2021}
}
