'''Problem: Demonstrate polymorphism by defining a 
method fuel_type in both Car and ElectricCar classes, 
but with different behaviors.'''


class Car:
    def __init__(self, brand, model):   #Constructor
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return f"{self.__brand} (T)" 
    
    def full_name(self):
        return f"{self.__brand}, {self.model}"
    
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