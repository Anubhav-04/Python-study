# WAP in python to create a class representing vector of n dimentions
# and overload the + and * operator which calculate the sum and .product

class Vectors:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def __add__(self,v2):
        return Vectors(self.i + v2.i , self.j + v2.j , self.k + v2.k)

    def __mul__(self,v2):
        dotProduct = Vectors(self.i * v2.i , self.j * v2.j , self.k * v2.k)
        crossProduct = Vectors(self.j * v2.k - self.k * v2.j , self.i * v2.k - self.k * v2.i ,self.i * v2.j - self.j * v2.i)
        return f"Dot product = {dotProduct} and Cross Product = {crossProduct}"

    def __str__(self):
        return f"{self.i}i {self.j}j {self.k}k"
    def __len__(self):
        return 3
    

v1 = Vectors(2,4,6)
v2 = Vectors(4,6,8)
print(f"Sum of two vectors is = {v1+v2}")
print(v1*v2)
print(f"length of vector = {len(v1)}")
    