''' Problem: Create a Car class with attributes like 
brand and model.Then create an instance of 
this class.'''

class Car:
    def __init__(self, brand, model):   #Constructor
        self.brand = brand
        self.model = model

    
my_car = Car("Maruti Suzuki", "Alto 800")
print(my_car.brand)
print(my_car.model)

print()

my_second_car = Car("TATA", "Safari")
print(my_second_car.brand)
print(my_second_car.model)