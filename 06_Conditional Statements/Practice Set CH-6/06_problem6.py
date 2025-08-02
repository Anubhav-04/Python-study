#WAP in python to calculate the grades from the marks
#Marks system
# 90-100 --- A
# 80-90 ---- B
# 70-80 ---- c
# 60-70 ---- D
# 50-60 ---- E
# <50 ------ F

marks = int(input("Enter your marks - "))

if(marks<=100 and marks>=90):
    print("A grade")
elif(marks<90 and marks>=80):
    print("B grade")
elif(marks<80 and marks>=70):
    print("C grade")
elif(marks<70 and marks>=60):
    print("D grade")
elif(marks<60 and marks>=50):
    print("E grade")
else:
    print("F grade")
print("The End!!!")
