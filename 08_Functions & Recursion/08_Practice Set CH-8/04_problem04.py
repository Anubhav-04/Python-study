#WAP in python to create function to print the following pattern
pattern ="*"
def patternDesign(n):
    if(n==0):
        return 0
    print(pattern*n)
    patternDesign(n-1)
a=int(input("Enter no of lines :- "))
patternDesign(a)