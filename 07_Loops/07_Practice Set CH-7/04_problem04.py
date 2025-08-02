#WAP in python to print the sum of first n natural number using while loop

n = int(input("Enter the number :- "))
sum = 0
i = 1
while(i<=n):
    sum = sum + i
    i = i+1
print (f"Sum of first {n} natral number is = {sum}")

#WAP in python to calculate the factorial of a given number using for loop
fact = 1
for i in range(1,n+1):
    fact = fact*i

print(f"Factorial of {n} = {fact}")

