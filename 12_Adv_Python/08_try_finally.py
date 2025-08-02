#try with finallly

# finally executes regardless of execution of try and except block
# if there is any retrun statement in the try or except block 
# then also finally block execute inside the function

def readFiles(filename):
    try:
        with open(filename,'r') as f1:
            content = f1.read()
            print(content)
    except FileNotFoundError:
        print("File not found")
    finally:
        try:
            f1.close
            print("File is closed")
        except NameError:
            print("No file was opened so not closed")
readFiles("/Users/assar/Desktop/Python Study/09_Files Input and Output/01_file.txt")