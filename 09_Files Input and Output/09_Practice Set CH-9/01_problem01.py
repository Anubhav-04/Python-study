# WAP in python to check wheather given string is present in the file.

word = input("Enter the word to check :- ")

with open("/Users/assar/Desktop/Python Study/09_Files Input and Output/01_file.txt","r") as f:
    if(word in f.read()):
        print(f"'{word}' word is present in the file")
    else:
        print(f"'{word}' word is not present in the file")

