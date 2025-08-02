# WAP in python to create a class employee and add a salaryIncrement 
#method with a property decorator with setter which changes the
# values of the increment based on salary.

class Employee:
    def __init__(self,name,domain,oldSalary):
        self.name = name
        self.domain = domain
        self.oldSalary = oldSalary
        self.increment = .10
    
    # def salaryAfterIncrement(self):
    @property
    def salary(self):
        return self.oldSalary + self.oldSalary*self.increment
    @salary.setter
    def salary(self,newsalary):
        if(newsalary > self.oldSalary ):
            self.increment = (newsalary - self.oldSalary)/newsalary
        else:
            print ("New salary must be greater than old salary.")
    def salaryAfterIncrement(self):
        print(f"Old salary of employee = {self.oldSalary}")
        print(f"Increment in salary of the employee = {self.increment *100 :.2F}%")
        print(f"Salay after increment of the employee = {self.salary:.2f}")

emp1 = Employee("Anubhav kumar","Software Engineer",3500000)
emp1.salary = 4500000
print(emp1.name)
print(emp1.domain)
emp1.salaryAfterIncrement()