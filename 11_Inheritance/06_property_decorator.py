# property decorator and setter method

class engineer:
        @property
        def branches(self):
            return (f"Branch name = {self.branch}")
        @property
        def name(self):
             return(f"First Name - {self.fname} , Last Name - {self.lname}")
             
        @branches.setter
        def branches(self,values):
            self.branch = values
        
        @name.setter
        def name(self,values):
             self.fname = values.split(" ")[0]
             self.lname = values.split(" ")[1]


emp1 =engineer()

emp1.branches = "Computer Science & Engineering"
emp1.name = "Sushmita Das"
print (f"Branch - {emp1.branch}")
print(f"First Name - {emp1.fname}")
print(f"Last Name - {emp1.lname}")

