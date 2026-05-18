'''Problem: Write a program to find the maximum of the numbers
in a list using the reduce function.'''

from functools import reduce


lst = [3, 5, 5, 56, 764556, 6453653, 43434, 5344, 
       4324, 43242, 4234, 423445,5345634,543534]

def func(x,y):
    if(x>y):
        return x
    return y
    
    
    

result = reduce(lambda x,y: x if x>y else y, lst)
print(result)





