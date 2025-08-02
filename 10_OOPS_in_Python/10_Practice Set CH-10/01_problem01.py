# WAP in python to create a class programmer and store multiple programmer details working in Microsoft

class Programmer():
    organisation = "Microsoft"
    def __init__(self,name,salary,techs):
        l=[self.organisation,name,salary,techs]
        self.l =l
programmer1 = Programmer("Sushmita","1.5 cr","Data Analyst")
print(programmer1.l)

programmer2 = Programmer("Mounideepa","80 lpa","Human Resouce")
print(programmer2.l)

programmer3 = Programmer("Juhi"," 90 lpa","Delivery Agent")
print(programmer3.l)