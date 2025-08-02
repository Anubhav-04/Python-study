#WAP in python to print sum of n natural numbers using recursion function

n = int(input("Enter value of n :- "))

def sumofNnautalnos(k):
    if(k==0):
        return 0
    else:
        return k + sumofNnautalnos(k-1)
    
print(f"Sum of first {n} natural numbers = {sumofNnautalnos(n)}")