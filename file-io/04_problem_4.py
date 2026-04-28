with open("file.txt") as f:
    data = f.read()
    data = data.replace("Donkeys","#####")
    data = data.replace("Donkey","#####")

with open("file.txt", "w") as f:
    f.write(data)