'''Problem: Create an ElectricCar class that inherits from 
the Car class and has an additional attribute.'''



class Car:
    def __init__(self, brand, model):   #Constructor
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return (f"{self.brand}, {self.model}")
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size



tesla = ElectricCar("Tesla", "Model X", "100 kWh")
print(tesla.full_name())
print(f"Battery Size : ~{tesla.battery_size}")