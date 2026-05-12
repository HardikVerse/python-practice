'''Problem: Write a class Vector representing a vector of n dimensions. 
Overload the + and * operator which calculates the sum and the dot(.) 
product of them.'''


class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, v2):
        return Vector(self.i + v2.i, self.j + v2.j, self.k + v2.k )
        
    def __mul__(self, v2):
        return (self.i * v2.i + self.j * v2.j + self.k * v2.k )
        
    def __str__(self):
        return f"{self.i}i\u0302 + {self.j}j\u0302 + {self.k}k\u0302"
    


v1 = Vector(5,6,7)
print(v1)
v2 = Vector(5,6,0)
print(v2)

print(f"Sum: {v1 + v2}")
print(f"Dot Product: {v1*v2}")
        
        

        

        