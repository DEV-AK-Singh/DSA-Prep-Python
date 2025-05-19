class Car: 
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.model = model
        self.year = year  

    def get_brand(self):
        return self.__brand    

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"

    @property
    def brand(self):
        return self.__brand    

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery, rangeInKM):
        super().__init__(brand, model, year)
        self.battery = battery
        self.rangeInKM = rangeInKM

    def charge(self):
        self.battery = 100

    def __str__(self):
        return f"{self.brand} {self.model} {self.year} {self.battery} | {self.range}"    

    @staticmethod
    def drive():
        print("Driving")    

my_car = Car("Toyota", "Camry", 2022)
my_ev_car = ElectricCar("Tesla", "Model 3", 2022, 100, 200)

# print(my_car.brand)
# print(my_car.get_brand())
# ElectricCar.drive()

print(isinstance(my_ev_car, ElectricCar))
print(isinstance(my_ev_car, Car))

class hybridCar(Car, ElectricCar):
    def __init__(self, brand, model, year, battery, rangeInKM):
        super().__init__(brand, model, year)
        self.battery = battery
        self.rangeInKM = rangeInKM