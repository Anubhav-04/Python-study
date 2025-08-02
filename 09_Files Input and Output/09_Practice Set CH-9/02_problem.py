#WAP in python to update the high score in a file when the user play the game.

import random

def game():
    score = random.randint(1,100)
    with open("/Users/assar/Desktop/Python Study/09_Files Input and Output/09_Practice Set CH-9/02_highScore.txt","r") as f :
        highScore = f.read()
        if(highScore != ""):
            highScore = int(highScore)
        else:
            highScore = 0
        print(f"Your score is = {score} and high score is = {highScore}")
        if(score>highScore):
            with open("/Users/assar/Desktop/Python Study/09_Files Input and Output/09_Practice Set CH-9/02_highScore.txt","w") as f :
                f.write(str(score))
            return score
        else:
            print(f"Your score is less = {score} than high score = {highScore}" )
            return score

game()