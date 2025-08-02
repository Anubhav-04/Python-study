#Operator Overloading

class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self,num):
        return self.n + num.n
    def __mul__(self,num):
        return self.n * num.n

n1 = Number(5)
n2 = Number(6)
print(n1+n2)
print(n1*n2)

class Strings:
    def __init__(self,s):
        self.s = s
    def __len__(self):
        return len(self.s)

s = Strings("Anubhav")
print(len(s))
