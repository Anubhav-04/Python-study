# Example of Multi Level Inheritance

class electronics :
    def __init__(self,type,power):
        self.type = type
        self.power = power
    def displayVersion(self):
        print(f"Type of Electronics : - {self.type}")
        print(f"Power of Electronics : - {self.power}")
class brand(electronics):
    def __init__(self, type, power,brandName,version):
        super().__init__(type, power)
        self.brandName = brandName
        self.version = version
    def displayBrand(self):
        self.displayVersion()
        print(f"Brand name - {self.brandName}")
        print(f"Version of brand - {self.version}")
class model(brand):
    def __init__(self, type, power, brandName, version,modelName,YearofRelease):
        super().__init__(type, power, brandName, version)
        self.modelName = modelName
        self.YearofRelease = YearofRelease
    def displayModel(self):
        self.displayBrand()
        print(f"Model of the vehicle - {self.modelName}")
        print(f"Release year of the vehicle - {self.YearofRelease}")

Vehicle1 = model("EV","590 HP","Mahindra","1.0","Mahindra EV-6",2024)
Vehicle1.displayModel()