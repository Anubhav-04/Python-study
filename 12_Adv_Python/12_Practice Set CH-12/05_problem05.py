#WAP in python to write the multiplication table in the file.txt
try:
    number = int(input("Enter your number :- "))

    multiplicationTable = [number*i for i in range(1,11)]

    with open("12_Adv_Python/12_Practice Set CH-12/Tables.txt",'a') as f1:
            f1.write(f"table of {number}--{str(multiplicationTable)} \n")
except Exception as e:
    print(e)
finally:
    try:
        f1.close()
    except:
        print("Not Required to close")
    