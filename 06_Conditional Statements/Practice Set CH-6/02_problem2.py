#WAP in python to find out wheather a student is passed if he secures 40% marks
#overall and 33% marks in each subject.Consider 3 subjects.

science = int(input("Enter marks of science subject :- "))
maths = int(input("Enter marks of maths subject :- "))
computer = int(input("Enter marks of computer subject :- "))

sum = science + maths + computer

if(sum/3 >= 40 and science >=33 and maths >=33 and computer >= 33):
    print("Congratulations you have passed.")
    print("You are promoted!!!")
else:
    print("You failed the exam.")
    print("Work hard study more.")
print("Thankyou!!!")