#WAP in python to create a 2-D vector and use it to create a 3-D vector

class TwoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show2DVectorParams(self):
        print(self.i)
        print(self.j)
class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show3DVectorParams(self):
        self.show2DVectorParams()
        print(self.k)
vector = ThreeDvector(4,6,8)
vector.show3DVectorParams()