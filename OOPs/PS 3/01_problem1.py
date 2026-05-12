'''Question:- Create a class (2-D vector) and use it 
to create another class representing a 3-D vector.'''




class Two_D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Three_D(Two_D):
    def __init__(self, x, y, z):
        self.z = z
        super().__init__(x, y) 

    def show(self):
        print(f"{self.x}i + {self.y}j + {self.z}k")

      

v1 = Two_D(5,5)
v2 = Three_D(5,5,4)
v2.show()
