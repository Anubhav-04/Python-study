# WAP in python to create a class which is capable of finding squares, cubes and square root oa number.
import math
class MathsOperations():
    def __init__(self,num):
        self.square = num*num
        self.cube = num*num*num
        self.sqRoot = math.sqrt(num)
    @staticmethod
    def greet():
        print("Hello user!")
n = int(input("Enter your number = "))
number1 = MathsOperations(n)
number1.greet()
print(f"Square of {n} = {number1.square}")
print(f"Cube of {n} = {number1.cube}")
print(f"Square Root of {n} = {number1.sqRoot}")