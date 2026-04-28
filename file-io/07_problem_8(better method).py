'''Question:- Write a program to find out 
the line number where python is present. '''


with open("logfile.txt") as f:
    lines = f.readlines() 

line_count = 1
for line in lines:
    if ("Python" in line):
        print(f"Python is present at line {line_count}")
        break
    line_count += 1
        
else:
    print("Not found in any line")


