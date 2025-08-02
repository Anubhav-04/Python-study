# WAP in python to add multiple names inside an empty dictionary

namesAndHobby = {}
person1 = input("Enter your name :- ")
hobby1 = input("Enter your hobby :- ")
namesAndHobby.update({person1:hobby1})
person2 = input("Enter your name :- ")
hobby2 = input("Enter your hobby :- ")
namesAndHobby.update({person2:hobby2})
person3 = input("Enter your name :- ")
hobby3 = input("Enter your hobby :- ")
namesAndHobby.update({person3:hobby3})
person4 = input("Enter your name :- ")
hobby4 = input("Enter your hobby :- ")
namesAndHobby.update({person4:hobby4})
# namesAndHobby = {
#     person1:hobby1,
#     person2:hobby2,
#     person3:hobby3,
#     person4:hobby4
# }

print(namesAndHobby)
