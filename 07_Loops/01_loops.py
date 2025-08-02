# while loops

# print numbers upto 10

a = 1
while(a<=10):
    print(a)
    a = a+1

userDetails = ["Swastik",10,"3-05-2015","Patna"]
i=0
while(i<len(userDetails)):
    print(userDetails[i])
    i=i+1

# for loops

for i in range(5):
    print(i)

#For loops with list
for item in userDetails:
    print(item)
#for loops with range(startrange,stoprange,stepsize)
for i in range(0,100,5):
    print(i)
#for loops to iterate string
name = "ANUBHAVKUMARGUPTA"
for i in name:
    print(i)