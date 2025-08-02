#WAP in python to find wheather the given username is of 10 characters or not.

username = input("Enter username - ")
if(len(username) <= 10):
    print("Valid username.")
    print("Welcome to our site.")
else:
    print("Invalid username.")