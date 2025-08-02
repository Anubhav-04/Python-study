#WAP in python to generate multiplication tables in different files from 2-20

for i in range(1,21):
    with open(f"/Users/assar/Desktop/Python Study/09_Files Input and Output/09_Practice Set CH-9/03_Tables/Table-{i}.txt","w") as tables:
        j=1
        while(j<=10):
            content = f"{i} X {j} = {i*j}\n"
            tables.write(content)
            j = j+1

    