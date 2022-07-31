f = open("demoFile.txt", "rt")
lines = f.readlines()
l = []
for line in lines:
    l.append(line[:-1])
for li in l:
    print(li)

# content = f.read()  # f.read(10) that is till10th index
# for line in f:
#     print(line, end="")
# print(content, type(content))
f.close()
print("\n")
print("readline()")
f = open("demoFile.txt", "rt")
print(f.readline())
lines = f.readlines()
print(lines)
f.close()
