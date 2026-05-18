'''Problem: Write a program to filter a list of numbers which 
are divisible by 5.'''


lst = [5, 4, 55, 60, 69, 1042.]

sort_list = list(filter(lambda x : x % 5 == 0, lst))
print(sort_list)