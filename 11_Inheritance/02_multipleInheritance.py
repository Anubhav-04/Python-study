#Multiple Inheritance

'''
class Running:
    print("He is running")
class Walking():
    print("He is Walking")
class Human(Running,Walking):
    print("He is healthy man")

Rohan = Human()

class Mother :
    M_name = "Mounika Singh"
class Father:
    F_name = "Sanjay Singh"
class Child(Mother,Father):
    C_name = "Raja Singh"

Child1 = Child()
print(f"Name :- {Child1.C_name}")
print(f"Father Name :- {Child1.F_name}")
print(f"Mother Name :- {Child1.M_name}")
'''

class logger:
    def log(self,message):
        print(f"LOG : {message}")
class databaseConnector:
    def connect(self):
        print("Database started!!!")
    def disconnect(self):
        print("Logged out Successfully.")
class DatabaseLogger(logger,databaseConnector):
    def saveData(self,data):
        self.connect()
        print(f"Saving Data : {data}")
        self.log(f"Data Saved : {data}")
        self.disconnect()
db_Logger = DatabaseLogger()
db_Logger.saveData({"user": "Anubhav", "action": "login"})