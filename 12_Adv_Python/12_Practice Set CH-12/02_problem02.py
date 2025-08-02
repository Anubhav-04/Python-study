#WAP in python to print the third fifth and 
# seventh element of the list

girlsName = ['Pooja','Rani','Soumi','Pallavi','Mounika','Rajni','Sarita','Anamika','Barsha','Chandani']

for index , item in enumerate(girlsName):
    if(index + 1 in (3,5,7)):
        print(f"{index+1} ------ {item}")
