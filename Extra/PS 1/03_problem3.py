'''Problem: Write a list comprehension to print a list which 
contains the multiplication table of a user entered number.'''


try:
    num =  int(input("Enter number: "))
    table_list = [i*num for i in range(1, 11)]
    print(table_list)

except ValueError:
    print("Please enter a integer.")

except Exception as e:
    print(e)

