import random

computerGuess = random.randint(1,100)
count =0
def guess():
    global count
    userGuess = int(input("Enter your guess = "))
    count += 1
    if(userGuess < computerGuess):
        print("Too low! Try Again!!")
        guess()
    elif(userGuess > computerGuess):
        print("Too High! Try Again!!")
        guess()
    elif(userGuess == computerGuess):
        print("You win")
        print(f"Total no of guesses = {count}")
guess()
    

