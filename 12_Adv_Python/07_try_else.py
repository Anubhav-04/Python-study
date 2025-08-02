# try with else

try:
    a = int(input("Enter a number : - "))
    print(a)
except Exception as e:
    print(e)

else:
    print(a*2) #if try block runs successfully then only it will execute else not
    