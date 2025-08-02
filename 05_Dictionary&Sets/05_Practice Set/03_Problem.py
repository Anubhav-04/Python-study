# WAP in python to check can we have 18 as int and 18 as string in same set

s = set()
num = 18
s.add(num)
str = "18"
s.add(str)

# num = input("Enter number 18 :- ")
# s.add(int(num))
# num = input("Enter number 18 :- ")
# s.add(num)
print(s)

# What will be length of following set

a = set()
a.add(20)
a.add(20.0)
a.add('20')
print(a,len(a))

#What is the type of s = {}

b = {}
print(type(b))