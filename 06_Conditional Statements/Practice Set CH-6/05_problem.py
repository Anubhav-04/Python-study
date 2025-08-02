#WAP in python to check wheather the given name is present in the list or not

nameList = ["Sita","Geeta","Anjali","Sushmita","Pammi"]

enterName = input("Enter your name - ")

if(enterName in nameList):
    print("Yes your name is present in the list.")
else:
    print("Your name is not present in the list.")