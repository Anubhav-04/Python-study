# Recursion

#Using recursion function to find out factorial

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

num1 = int(input("Enter any number :- "))
print(f"Factorial of {num1} = {factorial(num1)}")