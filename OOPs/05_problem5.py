'''Create student class that takes name & 
marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
And also display the grade.'''


class Student:
    def __init__(self, name, math, sci, ssc):
        self.name = name
        self.math_marks =  math
        self.science_marks =  sci
        self.ssc_marks =  ssc
    
    
    def get_marks(self):
        print("\nStudent marks in subjects:") 
        print(f"\tMathematics : {self.math_marks}")
        print(f"\tScience : {self.science_marks}")
        print(f"\tSocial Science : {self.ssc_marks}\n")


    def mean(self):
        total = (self.math_marks)+(self.science_marks)+(self.ssc_marks)
        avg = total/3
        return avg
    
    def grade(self):
        avg = self.mean()
        if(avg >=75):
            return "A"
        elif(avg >=50):
            return "B"
        else:
            return "C"
    
    def display(self):
        print(f"Name : {self.name}\n")
        print("Marks of Subjects:")
        print(f"\t Mathematics : {self.math_marks}")
        print(f"\t Science : {self.science_marks}")
        print(f"\t Social Sciecne : {self.ssc_marks}\n")
        print(f"Mean Marks : {self.mean():.2f}")
        print(f"Grade : {self.grade()}")


s1 = Student("Puri Lal Lodha", 66, 57, 80)
s1.display()

