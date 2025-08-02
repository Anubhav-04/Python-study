# Using with statement to open a file

with open("/Users/assar/Desktop/Python Study/09_Files Input and Output/01_file.txt","r") as f:
    print(f.read())
#we dont have to explicitly close the file it automatically closes when coming out of the with statement.
    