'''Problem: Add a static method to the Car 
class that returns a general description 
of a Car.''' 


class Car:

    total_car = 0

    def __init__(self, brand, model):   #Constructor
        self.__brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return f"{self.__brand}" 
    
    def full_name(self):
        return f"{self.__brand}, {self.model}"
    
    @staticmethod
    def gen_description():
        return "Car is used for transportation."

    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charger"



tesla = ElectricCar("Tesla", "Model X", "100 kWh")
print(tesla.full_name())
print(f"Battery Size : ~{tesla.battery_size}")
print(tesla.fuel_type())

print()

tiago = Car("TATA", "Tiago")
print(tiago.full_name())
print(tiago.fuel_type())

print(Car.gen_description())