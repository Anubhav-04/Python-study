# Multi Level Inheritance

class Person:
    def __init__(self,name,address,age,sex):
        self.name = name
        self.address = address
        self.age = age
        self.sex = sex
    def details(self):
        print(f'''
                Name - {self.name}
                Address - {self.address} 
                Age - {self.age}
                Sex - {self.sex}           
''')

class Employee(Person):
    def __init__(self,name,address,age,sex,empId,skills):
        super().__init__(name,address,age,sex)
        self.empId = empId
        self.skills = skills
    def empDetails(self):
        self.details()
        print(f'''
                Employee Id - {self.empId}
                Skills - {self.skills}
''')

class Manager(Employee):
    def __init__(self, name, address, age, sex, empId, skills,teamSize,task):
        super().__init__(name, address, age, sex, empId, skills)
        self.teamSize = teamSize
        self.task = task
    def mgrWork(self):
        self.empDetails()
        print(f"Team Size = {self.teamSize} and task - {self.task}")

Manager1 = Manager("Jhon Doe","Dalal Street",46,"M",7890,"Data Analyst PlSql","15 emps","Sprint work on Wednesday")
Manager1.mgrWork()