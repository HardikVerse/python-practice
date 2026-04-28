bad_word =["ghade","donkey","gande"]

with open("for_problem_5.txt") as f:
    data = f.read()
for word in bad_word:
    data = data.replace(word,"#"*len(word))
    
with open("for_problem_5.txt","w") as f:
    f.write(data)