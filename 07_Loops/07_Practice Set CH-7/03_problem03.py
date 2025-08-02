#WAP in python to print wheather a given number is prime or not

num = int(input("Enter a number :- "))
i = 0
for i in range (2,num):
    if(num%i ==0 ):
        print(f" {num} is not prime number")
        break
else:
    print(f" {num} is prime number")