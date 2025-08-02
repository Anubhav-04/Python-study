#WAP in python to check wheather the contents of the two different sample files are same

with open("09_Files Input and Output/09_Practice Set CH-9/04_sample.txt","r") as r1:
    content1 = r1.read()
with open("09_Files Input and Output/09_Practice Set CH-9/04_sample_copy.txt","r") as r2:
    content2 = r2.read()

if(content1 == content2):
    print("Yes both the files are same")
else:
    print('No both are different files')