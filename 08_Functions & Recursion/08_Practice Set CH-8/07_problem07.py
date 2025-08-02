#WAP in python to print multiplication table creating function

number = int(input("Enter the number :- "))

def mulTable(n,i):
        if(i==11):
            return exit 
        print(f"{n}X{i}={n*i}")
        i=i+1
        mulTable(n,i)
mulTable(number,1)