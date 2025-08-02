#WAP in python to greet all the members stored in the list whose names started with 'S'

persons = ["Awantika","Subhadra","Sonia","Prajakta","Monika","Sushmita"]

i = 0
for i in persons:
    if(i[0]=="S"):
        print(f"Hello {i} goodmorning Have a nice day")