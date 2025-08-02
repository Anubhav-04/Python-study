#Fuction definition

def greet ():
    print("Hello iam function greet")
# Function calling
greet()

#Function with arguments
def greetings (name):
    print(f"Hello {name} iam function with arguments")

greetings("Anubhav Gupta")

#Function with multiple arguments
def addition (a,b):
    sum = a+b
    print(f"{a}+{b}={sum}")
num1 = int(input("Enter first number :- "))
num2 = int(input("Enter second number :- "))
addition(num1,num2)

#Function with return statement
def multilication(c,d):
    prod = c*d
    return prod
product = multilication(num1,num2)
print(f"{num1}*{num2}={product}")

#Function with default argument
def update(condition="Default update"):
    print("System is updated by "+condition)

update()
update("Manual update")
