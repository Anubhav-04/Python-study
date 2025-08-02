#WAP in python to wipe out the contents from a file 

#WAP in python to make a copy of 04_sample.txt

with open("09_Files Input and Output/09_Practice Set CH-9/10_emptyFile.txt","r") as r:
    content = r.read()
    if(content != ""):
        content = ""
with open("09_Files Input and Output/09_Practice Set CH-9/10_emptyFile.txt","w") as w:
    w.write(content)