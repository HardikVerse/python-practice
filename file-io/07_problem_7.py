'''Question:- Write a program to find out 
the line number where python is present. '''


with open("logfile.txt") as f:
    i = 1
    line = f.readline()
    
    while True:
        if("Python" in line):
            indx = line.find("Python")
            print(f"Python present at line {i} and at index {indx}")
            line = f.readline()
        elif(line == ""):
            break
        else:
            print(f"Not found in line {i}")
            line = f.readline()
        i += 1

