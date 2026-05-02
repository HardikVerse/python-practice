"""Create a class “Programmer” for 
storing information of few programmers
working at Microsoft."""


class Programmer :
    company = "Microsoft"
    def __init__(self, name, age, salary):
        self.name = name 
        self.age = age
        self.salary = salary


p1 = Programmer("DJ Alok", "34", "6LPA")
print(p1.company)
print(p1.name, p1.age, p1.salary)