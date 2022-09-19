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


#****************Built in functions in python********************
#abs()
print(abs(-2))
print(abs(3-4j))
print(abs(3-1j))

#all()  Return true if all the elements of a given iterable( List, Dictionary, Tuple, set, etc) are True else it returns False
l=[1,2,3,4]
print(all(l))   #true
l=[1,0,2,3]
print(all(l))   #false
#for empty list return true always

#any()  Returns True if any of the items is True.
print(any(l))   #true
l=[False,0,0]
print(any(l))   #false  
#for empty list return false always

#bin()   returns the binary string of a given integer.
print(bin(7))      #0b111
print(bin(7)[2:])  #111

#bool()  It returns True if the parameter or value passed is True.
# It returns False if the parameter or value passed is False.
print(bool(True))
print(bool(False))


#eval()
evaluate = 'x*(x+1)*(x+2)'
print(evaluate)
print(type(evaluate))
x,y= 3,5
print(type(x))
expression = eval(evaluate)
print(expression)
print(type(expression))
print(eval(f"x+y"))

#float()
print(float(23),type(float(23)))
print(float("23"),type(float("23")))
print(str(23),type(str(23)))

a=23
b=23
print(id(a))  #same
print(id(b))  #same

#round()
print(round(23.4))
print(round(23.5))
print(round(23.6))


#max() min()
print(max(2,1,4,53,2))
print(min(2,1,4,53,3))
print(min(2,0.4,1,4,53,3))

#pow()
print(2**3)
print(pow(2,3))

#sorted()   always returns a list with the elements in a sorted manner, without modifying the original sequence.
print(sorted([3,2,1,5,53,1,7]))
print(sorted([3,2,1,5,53,1,7],reverse=True))


