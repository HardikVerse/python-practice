'''Problem: Modify the Car class to encapsulate the brand attribute,
making it private, and provide a getter'''



class Car:
    def __init__(self, brand, model):   #Constructor
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return f"{self.__brand} (T)" 
    
    def full_name(self):
        return (f"{self.__brand}, {self.model}")
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size



tesla = ElectricCar("Tesla", "Model X", "100 kWh")
print(tesla.get_brand())
print(tesla.full_name())
print(f"Battery Size : ~{tesla.battery_size}")