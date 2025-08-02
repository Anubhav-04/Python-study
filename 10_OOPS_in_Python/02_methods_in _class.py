#Methods in class

class NewJoinee :
    department = "Human Resource"
    level = "Level-1"
    ops = "Hiring an outsourcing process"
    def __init__(self): # --- (Also known as Constructor) #--- dunder method which is 
        #automatically called when any instance is created.
        print("Starting of the hiring process") 
    def operations(self): #- self argument refers to the instance of the class 
        # it is automatically passed with the function call from the instance.
        print(self.ops)
    @staticmethod #-- Whenever we dont want instance intervention in the function 
        #call we make the static method.
    def greet(): 
        print("Hi Good morning")

joinee1 = NewJoinee()
joinee1.name = "Ashmita Sharma"
joinee1.greet()
print(joinee1.name)
print(joinee1.department)
print(joinee1.level)
joinee1.operations() #------- method call --- NewJoinee.operations(joinee1)