# f=open("data.txt")

# # print(f.readline())

# for line in f:
# 	print(line)

# f.close()

# #file closing automatically using with keyword
# with open("data.txt") as f:
# 	print(f.read(10))  #first 10 char including spaces and new line char
# 	print(f.read(10))  #next 10 characters
# 	f.seek(20)         #move cursor to 20th position
# 	# print(f.read())
	
# #wirting in file
# with open("data2.txt","w") as f:
# 	f.write("omkar")
# 	f.write("""my name is omkar
# I am student ata Pce panvel
# I am expert at hello world""")

# #appending data 
# with open("data2.txt","a") as f:
# 	f.write("omkar")
# 	f.write("""my name is omkar
# I am student ata Pce panvel
# I am expert at hello world""")
 
 
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('Welcome to Python file handling.\n')

lines = ['Hello, World!\n', 'Welcome to Python file handling.\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)