# Inheritance in Python

class Employees:
    def __init__(self,name,address,Age,organisation):
        self.name = name
        self.address = address
        self.Age = Age
        self.organisation = organisation

class SDE(Employees):
    department = "Software Developer Engineer"
    project = "Netflix"
    salary = "19 lpa"
    def languages(self,language):
        self.language = language
        return (f"{self.name} is a good employee an well versed with {self.language} knowledge.")
class HR(Employees):
    department = "Human Resource Admin"
    project = "HRA"
    salary = "15 lpa"
    def languages(self,language):
        self.language = language
        return (f"{self.name} is a good employee an well versed with {self.language} knowledge.")

print("Employee 1 -----------------------------------------")
emp1 = SDE("Raja Kumari","Bangalore",36,"Google")
print(f"Name :- {emp1.name}")
print(f"Address:- {emp1.address}")
print(f"Age :- {emp1.Age}")
print(f"Organisation :- {emp1.organisation}")
print(f"Department :- {emp1.department}")
print(f"Project :- {emp1.project}")
print(f"Salary :- {emp1.salary}")
print(emp1.languages("Python"))

print("Employee 2 -----------------------------------------")
emp2 = HR("Shivani Kumari","Bangalore",28,"Microsoft")
print(f"Name :- {emp2.name}")
print(f"Address:- {emp2.address}")
print(f"Age :- {emp2.Age}")
print(f"Organisation :- {emp2.organisation}")
print(f"Department :- {emp2.department}")
print(f"Project :- {emp2.project}")
print(f"Salary :- {emp2.salary}")
print(emp2.languages("Data Science"))