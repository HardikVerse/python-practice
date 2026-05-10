'''Write a class “Calculator” capable of finding
square, cube and square root of a
number.'''




class Calculator:
    def __init__(self, n):
        self.n = n
        
    def sq(self):
        print(self.n**2)

    def cube(self):
        print(self.n**3)
    
    def sq_root(self):
        print(self.n**(1/2))
    

a = Calculator(4)
a.sq()
a.cube()
a.sq_root()