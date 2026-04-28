''' Question:- Write a program to read the text from a given file
 poems.txt and find out whether it contains the word twinkle.'''

with open("poems.txt") as f:
    if("twinkle" in f.read()):
        print("Contain")
    else:
        print("Not contain")


