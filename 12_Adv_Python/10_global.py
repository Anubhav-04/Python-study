#Using global keyword to change the values of the variable

a = 10

def num():
    global a #we can access the variable which is outside the function using global keyword
    a = 49
    return a
print(num())