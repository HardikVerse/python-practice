try:
    num =  int(input("Enter number: "))
    table_list = [i*num for i in range(1, 11)]
    
    with open("Table.txt", "a") as f:
        f.write(f"Table of {num}: {str(table_list)}\n")


except ValueError:
    print("Please enter a integer.")

except Exception as e:
    print(e)
