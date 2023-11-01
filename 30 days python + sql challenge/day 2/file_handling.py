# opening file

# read mode
print("Read Mode")
file = open('text.txt', 'r')

# line = file.readline()

# while line != "":
# 	print(line + "line")
# 	line = file.readline()

content = file.read()
print("content start ",  content, "content end")

file.close()

# write mode
print("Write Mode")

file = open('output.txt', 'w')
file.write(content)


file.close()

# append mode
print("Append Mode")

file = open('output.txt', 'a')
file.write("\n")
file.write(content)

file.close()

# 'with' statement

with open('output.txt', 'r') as file:
	content = file.read()
	print(content)

print('\n', end = '');

# Error handling with files
print("Error Handling")

try:
    with open('text.txt', 'r') as file:
        for line in file:
            print(line, end='')
        print('\n', end = '')
except Exception as e:
    print(e)

print("\n", end = '')

# reading specific characters
print("reading specific characters")

with open('text.txt', 'r') as file:
	print(file.read(10), '\n')

# writing multiple lines
print("Writing Multiple Lines")
lines = ['first line\n', 'second line\n', 'third line\n']

with open("file.txt", 'w') as file:
	file.writelines(lines)

with open("file.txt", 'r') as file:
	print(file.read(), '\n')

# working with binary files
print("Working with binary files")

with open("files/arch.png", 'rb') as img:
	data = img.read()

with open("files/newImg.jpg", 'wb') as newImg:
	newImg.write(data)

# checking if file exists
print("Checking if file exists")

import os
if os.path.exists('example.txt'):
	print("File exists", '\n')
else:	
    print("File does not exists",'\n')


# File pointer
print('File pointer')

print("pointer position -> ", end = '')
with open('text.txt', 'r') as file:
	file.readline()
	position = file.tell()

	print(f"position : {position}", '\n')

print("Re-positioning pointer using seek()")
with open("text.txt", 'r') as file:
	file.read(22)
	file.seek(0)
	print(file.read(5)) # read 5 character from 0th position
	print(file.readline())

