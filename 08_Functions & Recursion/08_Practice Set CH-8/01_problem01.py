#WAP to create a function to find out greatest of three numbers.
a = int(input("Enter First number :- "))
b = int(input("Enter Second number :- "))
c = int(input("Enter Third number :- "))

def greatest_of_Three(e,f,g):
    if(e>f and e>g):
        return e
    elif(f>e and f>g):
        return f
    else:
        return g
    
greatest = greatest_of_Three(a,b,c)
print(f"{greatest} is the greatest number among {a},{b},{c}")


