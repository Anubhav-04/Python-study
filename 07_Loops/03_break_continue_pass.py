#Using break statement 
# break statement is used to come out of the loop instantly.
planets = ("Earth","Mars","Jupitor","Saturn","Neptune","Uranus")
i=0
for i in planets:
    print(i)
    if i=="Saturn":
        break
print("Came out of loop")
print("***************$$$$$$$$$$$$$$$$$$$$$*********************")

#Using Continue statement
#continue statement is used to stop the current iteration of the loop and continue 
#with the next iteration.It instructs the program to skip this iteration.
for i in planets:
    if i == "Jupitor" :
        continue
    print(i)
print("Came out of loop")
print("***************$$$$$$$$$$$$$$$$$$$$$*********************")
#Using Pass statement
#pass statement is a null statement in python.
#It instructs to do nothing.
for i in planets:
    pass
print("Came out of loop")
print("***************$$$$$$$$$$$$$$$$$$$$$*********************")
