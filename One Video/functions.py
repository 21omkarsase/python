#function wiht argument type and return type

print(5 is 5)
print(1 is not 2)
a=5
print(id(a))

def add(num1: int, num2: int) -> int:
	"""this function calculates sum of two integers"""
	return num1 + num2
	
# def add(num1, num2):
	# return num1 + num2

num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

#default arguments
def func(age=0):
	print(f"my age is {age}")

func()
func(20)

#keyword arguments
def student(firstname,lastname):
	return f"my name is {firstname} {lastname}"

print(student(firstname="omkar",lastname="sase"))
print(student(lastname="sase",firstname="omkar"))

#************variable length arguments******* 
# *args (Non-Keyword Arguments)
def func(*argv):
	for i in argv:
		print(i)
		
func("omkar","pce")

# **kwargs (Keyword Arguments)
def func(**args):
	print(args)     
	print(type(args))        #dictionary
	for i,j in args.items():
		print(i,j)
		
func(first="omkar",last="sase")


#    default pass by value-->string integer variables
#    default pass by reference objects tuples lists dics

def set_list(list):
	list = ["A", "B", "C"]
	return list

def add(list):
	print(id(my_list))
	list.clear()
	# return list

my_list = ["E"]

print(set_list(my_list))

add(my_list)
print(my_list)

# Python code to demonstrate
# call by value


string = "Geeks"


def test(string):
	string = "GeeksforGeeks"
	
test(string)
print(string)

def func(f):
	del f
	pass
	
tu=(1,2,3,4)
func(tu)
print(tu)
