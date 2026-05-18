'''Problem: Write a program to input name, marks and phone 
number of a student and format it using the format function 
like below:
"The name of the student is Harry, his marks are 72 and contact 
number is 99999888"'''


name = input("Name: ")
marks = int(input("Marks: "))
contact_num = int(input("Contact Number: "))

output = "The name of the student is {0}, his marks are {1} and contact number is {2}".format(name, marks, contact_num)
print(output)

