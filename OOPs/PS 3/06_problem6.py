'''Problem: Write __str__() method to print the vector as follows:
7i + 8j +10k'''


class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i\u0302 + {self.j}j\u0302 + {self.k}k\u0302"
        

v1 = Vector(5,6,7)
print(v1)
