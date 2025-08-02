#Class and Objects

class Employees :
    organisation = "Google" #-------- class attribute
    technology = "Cloud Computing"

print("Details of Employee 1")
emp1 = Employees() #--------- Object/instance Creation
emp1.name = "Anubhav Kumar" #--------- instance attribute
print(emp1.name)   
print(emp1.organisation)
print(emp1.technology)

print("Details of Employee 2")

emp2 = Employees()
emp2.name = "Mounideepa dey"
emp2.tecnology = "Pl-SQL"
print(emp2.name)   
print(emp2.organisation)
print(emp2.technology) #---- Instance attribute is preferred over class attribute

