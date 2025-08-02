#WAP in python to check the word django presnt in which line no in log file

with open("/Users/assar/Desktop/Python Study/09_Files Input and Output/09_Practice Set CH-9/06_sampleLogFile.txt","r") as r:
    content = r.readlines()
lineno = 1
for line in content:
    if("django" in line):
        print("django present on line number = ",lineno)
        break
    lineno = 1+lineno
else:
    print("Not present")
