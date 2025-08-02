#WAP in python using list comprehension to print the 
# multiplication table of user entered number

number = int(input("Enter your number :- "))

multiplicationTable = [number*i for i in range(1,11)]
print(multiplicationTable)