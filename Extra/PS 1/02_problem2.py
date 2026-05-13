'''Problem: Write a program to print third, fifth and 
seventh element from a list using enumerate function.'''


numbers = [1, 2, 5, 65, 7, 8, 64, 65, 75, 342,]  #5,7,64


for i,item in enumerate(numbers, start=1):
    if i in (3, 5, 7):
        print(item)