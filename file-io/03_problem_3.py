'''Question:- Write a program to generate multiplication 
tables from 2 to 20 and write it to the
different files. Place these files 
in a folder for a 13 - year old.'''
    

def table(num):
    with open(f"Table/Table-{num}.txt", 'w') as f:
        for i in range(1,11):
            f.write(f"{num} x {i} =  {num*i}\n")
       
for n in range(2,21):
    table(n)







