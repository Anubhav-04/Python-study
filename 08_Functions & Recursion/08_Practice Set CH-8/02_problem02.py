#WAP in python to create function to convert celsius to fahrenheit.

tempinC = int(input("Enter temperature in degree celsius :- "))

def convertinFahrenheit(c):
    return ((c*9)/5) +32

print(f"Temperature in fahrenheit is = {convertinFahrenheit(tempinC)} degree F")
