'''Question:- Create a class 'Employee' and add salary 
and increment properties to it.
Write a method 'salaryAfterIncrement' method with a 
@property decorator with a setter which changes the 
value of increment based on the salary.'''



class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    @property
    def showinfo(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}") 

    
    

    def increment(self, percent):
        increase = (self.salary * percent) / 100
        self.salary += increase

        print(f"Increment of {percent}% done in salary")


mohan = Employee("Mohan",500)
mohan.showinfo
mohan.increment(10)
mohan.showinfo






class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100


e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print(e.increment)