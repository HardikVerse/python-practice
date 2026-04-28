with open("copy.txt") as f:
    content_1 = f.read()
with open("this.txt") as f:
    content_2 = f.read()

if (content_1 == content_2):
    print("Both file are same")
else:
    print("Both file are not same.")