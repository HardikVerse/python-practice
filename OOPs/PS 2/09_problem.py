'''Problem: Demonstrate the use of isinstance() to check if 
my_Tesla is an instance of a Car and an ElectricCar.'''


class Car:

    total_car = 0

    def __init__(self, brand, model):   #Constructor
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return f"{self.__brand}" 
    
    def full_name(self):
        return f"{self.__brand}, {self.__model}"
    
    @staticmethod
    def gen_description():
        return "Car is used for transportation."
    
    @property
    def model(self):
        return self.__model

    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charger"



tesla = ElectricCar("Tesla", "Model X", "100 kWh")

print(isinstance(tesla, ElectricCar))
print(isinstance(tesla, Car))
