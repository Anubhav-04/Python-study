#WAP in python to make a copy of 04_sample.txt

with open("09_Files Input and Output/09_Practice Set CH-9/04_sample.txt","r") as r:
    content = r.read()
with open("09_Files Input and Output/09_Practice Set CH-9/04_sample_copy.txt","w") as w:
    w.write(content)