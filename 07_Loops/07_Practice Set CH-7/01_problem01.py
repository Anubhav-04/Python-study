#WAP in python to print the multiplication table of the given number.

num = int(input("Enter a number :- "))
print(f"Multiplication table of the {num}")

i = 0
#Using for loop
print(f"Multiplication table of the {num} using for loop")
for i in range (1,11):
    print(f"{num} X {i} = {num * i}")
    i =+ 1
print("---------------******************---------------------")
# using while loop
j=1
print(f"Multiplication table of the {num} using while loop")
while(j<=10):
    print(f"{num} X {j} = {num * j}")
    j=j+1
print("---------------******************---------------------")
print(f"Multiplication table of the {num} using for loop in reverse order")
k=10
for i in range (1,11):
     print(f"{num} X {k} = {num * k}")
     k = k-1
print("---------------******************---------------------")