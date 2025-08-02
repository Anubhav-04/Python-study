#WAP in python to convert inches to cms

inch = float(input("Enter the length in inches :- "))

def convertinCMS(inch):
    return inch*2.54

print(f"{inch} inches in CMS = {convertinCMS(inch)} cm")