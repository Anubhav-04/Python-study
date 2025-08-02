#WAP in python to rename the file name
import os

oldName = "/Users/assar/Desktop/Python Study/09_Files Input and Output/09_Practice Set CH-9/demo.txt"

newName = "/Users/assar/Desktop/Python Study/09_Files Input and Output/09_Practice Set CH-9/11_newDemo.txt"

os.rename(oldName, newName)
print("Renamed successfully.")


# try:
#     os.rename(oldName, newName)
#     print("Renamed successfully.")
# except FileNotFoundError:
#     print("The file does not exist.")
# except FileExistsError:
#     print("A file with the new name already exists.")
# except PermissionError:
#     print("Permission denied.")

