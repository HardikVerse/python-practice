# Add a static method in problem 2, to greet the user with hello.




class Calculator:
    def __init__(self, n):
        self.n = n
        
    def sq(self):
        print(self.n**2)

    def cube(self):
        print(self.n**3)
    
    def sq_root(self):
        print(self.n**(1/2))
    
    @staticmethod
    def greet():
        print("Hello")

    

a = Calculator(4)
a.greet()
a.sq()
a.cube()
a.sq_root()