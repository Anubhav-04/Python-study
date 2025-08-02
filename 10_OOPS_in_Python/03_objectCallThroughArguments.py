# Instance call through Arguments.

class Animals():
    def __init__(self,name,type,place):
        self.name = name
        self.type = type
        self.place = place
Lion = Animals("Lion","Carnivorous","Forest")
print(f"{Lion.name} is {Lion.type} animal and lives in {Lion.place}")

Deer = Animals("Deer","Herbivorus","Forest")
print(f"{Deer.name} is {Deer.type} animal and lives in {Deer.place}")