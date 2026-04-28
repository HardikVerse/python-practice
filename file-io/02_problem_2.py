'''Question :- The game() function in a program 
lets a user play a game and returns the score
as an integer. You need to read a file
Hi-score.txt which is either blank or
contains the previous Hi-score. 
You need to write a program to update the Hiscore
whenever the game() function breaks the Hi-score.'''


import random

def game(x,y):
    score = random.randint(x,y)  


    print("Number is generating...")
    print(f"Score is {score}")


    with open("Hi-score.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

        if(score > hiscore):
            print("This is new score")
            with open("Hi-score.txt","w") as f:
                f.write(str(score))
            
        
game (1,69)

        
    





