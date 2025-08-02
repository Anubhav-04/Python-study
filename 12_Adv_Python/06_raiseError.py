#Raising Error

a = int(input("Enter a number : "))
b = int(input("Enter b number : "))

if(b==0):
    raise ZeroDivisionError("Hey this program is not meant for division with zero")
print(a/b)
