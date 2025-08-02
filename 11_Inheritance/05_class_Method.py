# Class Method -- A class method is the method which is 
# bound to a class not the object of the class.

# @classmethod decorator is used to create a class method

class number:
    a = 22
    @classmethod
    def num(cls):
        print(f"Class method number = {cls.a}")
num1 = number()
num1.a = 46
num1.num()