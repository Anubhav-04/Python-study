#WAP in python to create a class pets from class animal and further create a class Dog from class pets and add a method bark

class Animal:
    def show(self):
        print("I am a animal lover")
class Pets(Animal):
    def showPet(self):
        self.show()
        print("I have many pet animals")
class Dog(Pets):
    def bark(self):
        self.showPet()
        print("My dog is Barking")
pet = Dog()
pet.bark()