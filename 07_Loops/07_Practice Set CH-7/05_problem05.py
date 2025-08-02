# WAP in python to print the pattern
'''
PATERN NO :- 1
  *
 ***
*****

'''

n = int(input("Enter the number of lines :- "))
pattern = "*"
print("PATTERN NO 1")
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1),end="")
    print("")
print("-----------------------xxxxxxxxxxxxxxxxxxx-------------------------")

'''
PATERN NO :- 2
*
**
***
****
*****
'''
print("PATTERN NO 2")
for i in range(1,n+1):
    print(pattern*i)
print("-----------------------xxxxxxxxxxxxxxxxxxx-------------------------")

'''
PATERN NO :- 3
***
* *
***
'''
print("PATTERN NO 3")
for i in range(1,n+1):
    if(i==1 or i==n):
        print(pattern*n, end = "")
    else:
        print(pattern,end="")
        print(" "*(n-2),end="")
        print(pattern,end="")
    print("")

print("-----------------------xxxxxxxxxxxxxxxxxxx-------------------------")