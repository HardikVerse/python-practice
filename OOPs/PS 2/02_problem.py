'''Problem: Add a method to the Car class that displays
the full name of the car (brand and model).'''


class Car:
    def __init__(self, brand, model):   #Constructor
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return (f"{self.brand}, {self.model}")

    
my_car = Car("Maruti Suzuki", "Alto 800")
print(my_car.full_name())


print()

my_second_car = Car("TATA", "Safari")
print(my_second_car.full_name())

