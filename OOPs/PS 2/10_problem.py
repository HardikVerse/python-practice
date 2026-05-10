'''Question: Create two classes, Battery and Engine, and let the 
ElectricCar class inherit from both, demonstrating multiple inheritors.'''

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
    
class Battery:
    def battery_info(self):
        return "This is battery."
    
class Engine:
    def engine_info(self):
        return "This is engine."

class NormalCar(Car):
    def __init__(self, brand, model, tank):
        super().__init__(brand, model)
        self.tank = tank

    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charger"



tesla = ElectricCar("Tesla", "Model X", "100 kWh")
print(tesla.full_name())
print(f"Battery Size : {tesla.battery_size}")
print(tesla.fuel_type())
print(tesla.engine_info())
print(tesla.battery_info())

print()

tiago = NormalCar("TATA", "Tiago", "35 L")
print(tiago.full_name())
print(f"Tank Capacity : {tiago.tank}")
print(tiago.fuel_type())

