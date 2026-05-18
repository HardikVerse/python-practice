'''Problem: . A list contains the multiplication table of 7. 
Write a program to convert it to vertical string of same 
numbers.'''


try:
    num =  int(input("Enter number: "))
    table_list = [str(i*num) for i in range(1, 11)]
    result = ("\n").join(table_list)
    print(result)

except ValueError:
    print("Please enter a integer.")

except Exception as e:
    print(e)