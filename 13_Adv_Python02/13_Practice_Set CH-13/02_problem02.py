#WAP in python to store name address phone number and sex of 
# student in the following format using format method

name = input("Enter your name :- ")
address = input('Enter your address :- ')
phoneNumber = int(input("Enter your phone number :- "))
sex = input('Enter your gender :- ')
if(sex=='M'):
    M='man'
else:
    M='woman'
yoursData = 'Hi {} your belong to {} and you are {} straight {} , and your phone number is :- {}'.format(name,address,sex,M,phoneNumber)
print(yoursData)