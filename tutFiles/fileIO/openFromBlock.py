with open("readWrite.txt") as f:
    a = f.readlines()
    print(a)

f = open("readWrite.txt")
print(f.read())
f.close()
