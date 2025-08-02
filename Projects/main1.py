import random


print("Game Starts")
print("SNAKE WATER GUN")

'''
    SANAKE = -1
    WATER = 0
    GUN = 1

    -1,-1 ==== Draw
    -1,0 ==== lose
    -1,1 ==== Win

    0,-1 === win
    0,0 ====Draw
    0,1 ===win

    1,-1 ===== lose
    1,0 ===== lose
    1,1 ==== Draw

'''
compChoice = random.choice([-1,0,1])

print('''
    Choice 1 = SNAKE
    Choice 2 = WATER
    Choice 3 = GUN
''')

userEntry = input("Enter your choice from above :- ")

choiceDictionary = {
    "SNAKE":-1,
    "WATER":0,
    "GUN":1
}
#print(userChoice.upper())
userChoice = choiceDictionary[userEntry.upper()]
reverseChoiceDictionary = {
    -1 : "SNAKE",  
     0 : "WATER",
     1 : "GUN"
}

print(f" User Choice is : {reverseChoiceDictionary[userChoice]} \n Computer Choice is : {reverseChoiceDictionary[compChoice]} ")

if(compChoice==userChoice):
    print("It's Draw play again")
else:
    if(compChoice == -1 and userChoice == 0):
        print("You lose!!")
    elif(compChoice == -1 and userChoice == 1):
        print("You Win!!!")
    elif(compChoice == 0 and userChoice == 1):
        print("You Win!!!")
    elif(compChoice == 0 and userChoice == -1):
        print("You Win!!!")
    elif(compChoice == 1 and userChoice == 0):
        print("You lose!!")
    elif(compChoice == 1 and userChoice == -1):
        print("You lose!!")
    else:
        print("Something went unfortunate!")
    

