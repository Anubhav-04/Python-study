#WAP in python to find out 'django' word present in given log file.

with open("/Users/assar/Desktop/Python Study/09_Files Input and Output/09_Practice Set CH-9/06_sampleLogFile.txt","r") as r:
    content = r.read()
    if("django" in content):
        print("Yes word django is present in the log file")
    else:
        print("No word django is not present in the log file")