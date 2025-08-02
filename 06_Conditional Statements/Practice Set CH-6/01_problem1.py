#WAP in python to print greatest of four numbers

a = int(input("Enter number:- "))
b = int(input("Enter number:- "))
c = int(input("Enter number:- "))
d = int(input("Enter number:- "))

if(a>b and b>c and c>d):
    print(a," is greatest.")
elif(b>a and b>c and b>d):
    print(b," is greatest.")
elif(c>a and c>b and c>d):
    print(c," is greatest.")
else:
    print(d," is greatest.")

print("End of program.")