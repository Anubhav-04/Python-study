#WAP in python to create a class train which has methods book tickets, get status, and get fare details.
import random
class IRCTC():
    def getFareDetails(self,coaches):
        print("Fares from Dhanbad to Howrah")
        fares = {
            "generalCoach" : 120,
            "chairCar" : 540,
            "sleeper" : 320,
            "ac_Class1" : 1490,
            "ac_Class2" : 1220,
            "ac_Class3" : 980
        }
        if(coaches == "Gl"):
            return fares["generalCoach"]
        elif(coaches == "CC"):
            return fares["chairCar"]
        elif(coaches == "SL"):
            return fares["sleeper"]
        elif(coaches == "AC-1"):
            return fares["ac_Class1"]
        elif(coaches == "AC-2"):
            return fares["ac_Class2"]
        elif(coaches == "AC-3"):
            return fares["ac_Class3"]

    def bookTicket(self,name,age,sex,preference):
        self.name = name
        self.age = age
        self.sex = sex
        self.preference = preference
        self.pnrNo = random.randint(11111,99999)
        self.seatNo = random.randint(1,70)
        self.status = random.choice(["CNF","WL","RLWL"])
    
    def paymentGateway(self):
        if(self.preference == "GL"):
            seatPrice = 120
            gatewayPrice = 10
            tot_amount = seatPrice + gatewayPrice
            return tot_amount
        elif(self.preference == "CC"):
            seatPrice = 540
            gatewayPrice = 15
            tot_amount = seatPrice + gatewayPrice
            return tot_amount
        elif(self.preference == "SL"):
            seatPrice = 320
            gatewayPrice = 15
            tot_amount = seatPrice + gatewayPrice
            return tot_amount
        elif(self.preference == "AC-1"):
            seatPrice = 1490
            gatewayPrice = 45
            tot_amount = seatPrice + gatewayPrice
            return tot_amount
        elif(self.preference == "AC-2"):
            seatPrice = 1220
            gatewayPrice = 35
            tot_amount = seatPrice + gatewayPrice
            return tot_amount
        elif(self.preference == "AC-3"):
            seatPrice = 980
            gatewayPrice = 25
            tot_amount = seatPrice + gatewayPrice
            return tot_amount

    def PNRstatus(self,pnr):
        self.pnr=pnr
        if(self.pnr == self.pnrNo):
            return f"{self.name} {self.age} {self.sex} --- PNR NO :- {self.pnrNo} ------{self.preference} {self.seatNo} CNF"
Traveller1 = IRCTC()
coachPref = input("Enter your coach preference for fare details :- ")
print(f"Fare of {coachPref} coach is Rupees - {Traveller1.getFareDetails(coachPref)}")

print("press yes to proceed for booking")
consent = input("Enter yes to proceed for booking = ")
if(consent == "Y"):
    name = input("Enter your name = ")
    age = input("Enter your age = ")
    sex = input("Enter your sex = ")
    preference = input("Enter your preference = ")
    booking = Traveller1.bookTicket(name,age,sex,preference)
    #print(Traveller1.paymentGateway())
    payment = input(f"please pay Rupees {Traveller1.paymentGateway()} to proceed with your booking :- ")
    if(payment == "paid"):
        print(f"Booking successful for the {name} {age} {sex} ---- PNR NO - {Traveller1.pnrNo} ----- {preference} {Traveller1.seatNo} {Traveller1.status}")
print("To know the status of the booking")
booking = input("Enter Y to know your booking Status:- ")
if(booking == "Y"):
    print(Traveller1.PNRstatus(Traveller1.pnrNo))


