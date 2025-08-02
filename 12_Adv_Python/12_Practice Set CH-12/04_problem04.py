#WAP in python to display a/b where a and b are integers if
# b = 0 display infinite and handle Zerodivisionerror

a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
try:
    print(a/b)
except ZeroDivisionError:
    print("∞")
else:
    print("Program executed succesfully")