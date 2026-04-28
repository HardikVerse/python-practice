with open("logfile.txt") as f:
    content = f.read()
    content = content.lower()
if("python" in content):
    print("Yes, file contain python.")
else:
    print("No, it doesnt contain python.")

