#********************strings are immutable*******************

#*************Triple quotes for multiline*************
data='''name-->omkar
age-->20
residence-->thane
college-->pce
	 '''
print(data)


#*************accessing substring and character*************
str1="Expert at hello world"

print(str1)
print(str1[-1])  #charcter
print(str1[0])   #charcter
print(str1[0:9]) #substring
print(str1[-5:]) #substring	
print(str1[:6])  #substring
print(str1[0:len(str1):2]) # or [::2] #start end-1 increment
print(str1[14:9:-1])       # in reverse order
print(str1[::-1]) #string reverse  


#*************string concate and multiply*************
str2="Expert at copy-paste"

print(str1+" & "+str2) #concatenation
print((str1+" ")*3)    #string multiplication


#*************for loops in string*************
for ch in str1:
	print(ch,end=" ")
print("\n")


#*************string functions*************
str3="AASDF"
str4="234"

print(str3.isalpha())  #only alphabets(not even white space) are allowed
print(str4.isdigit())  #only digits(not even white space) are allowed
print(str4.isalnum())  #only alphabets and digits are allowed
print(str4.isdecimal(),"decimal")#decimal valule check
print(str3.isupper())  #are all captial
print(str3.islower())  #are all small
print(str1.upper())    #will convert string to uppercase
print(str3.lower())    #will convert string to lowercase
str3=str3.swapcase() #will convert upper to lower & vice-versa
print(str3.swapcase()) #will convert upper to lower & vice-versa

#replace replace(new,old,no_of_replaces) replace("hello","world",2)
new_str=str1.replace("hello world","copy paste")
print(new_str)

#find .find("pattern",start,end)
new_str="open to work open to work"
print(new_str.find("to"))
print(new_str.rfind("to"))

str5="          omkar           "

print(str5.lstrip())      #remove spaces from left
print(str5.rstrip())      #remove spaces from right    
print(str5.strip())  #remove spaces from both left and right

str5="expert at copy paste"
print(str5.endswith("paste"),str5) 
print(str5.endswith("y",6,14))  #endswith("pattern",start,end)

print(str5.startswith(" at",6,14))  #startswith("pattern",start,end)
print(str5[6:14])


#*************string reverse*************
print("".join(reversed(str3)))
print(str1[::-1])

#join function
str1="-".join(str1) #changing original string 
print(str1)

#****************updating string characters*************
#1
list1=list(str3)
list1[1]='Z'
list1[2]='Y'
str3=''.join(list1)
print(str3)

#2
str3=str3[0:1]+'a'+'b'+str3[3:]
print(str3)
2
#***********deletions of string character************
str3=str3[0:1]+str3[2:]

print(str3)
del str3     #will delete entire string


#*************Escape sequencing*************
print("my name is 'omkar'")
# print("my name is "omkar"") can't use double quotes in double quotes or single quotes in single quotes
print("my name is \"omkar\"")
print("c:\\python\\one_video")  #escaping backslashes
print("new line")
print("omkar\nsase")            #new line
print("hello\tuser")            #\t adds space(tab-width)
print(r"my name is\nomkar")     #will print string in its raw format ignoring \n as a new line


#*************string formatting*************
name="omkar"
age="20"
college="PCE"
print("my name is {}. I am {} years old and my college name is {}.".format(name,age,college))
print("my name is {1}. I am {0} years old and my college name is {2}.".format(age,name,college))
print("my name is {n}. I am {a} years old and my college name is {c}.".format(c=college,n=name,a=age))

num1,num2,ans=2,3,2+3
print(f"The addition of {num1} and {num2} results {ans}.")

#*************formating integers & floats*************
str7="{0:b}".format(7)
str8="{0:e}".format(26545)

print(str7)          #will print binary val of 7 as a string
print(str8)          #will print exponential form of a number as a string


#**************Rounding of integers***************
str9="{0:.1f}".format(123.2343)

print(str9)



#***********formatting using %*************

variable = '15'
string = "Variable as string = %s" %(variable) # %s for string

print (string)
print ("Variable as raw data = %r" %(variable)) # %r for '15'

variable = int(variable) 
string = "Variable as integer = %d" %(variable)

print (string)
print ("Variable as float = %f" %(variable))
print ("Variable as printing with special char = %c" %('y'))
print ("Variable as hexadecimal = %x" %(variable))
print ("Variable as octal = %o" %(variable))


#******************template class in python******************
from string import Template

student_list=['omkar','sairaj','rohan','abhishek','harsh','abhay']
name_info=Template("my name is $name")
for i in student_list:
	print(name_info.substitute(name=i))
	
	
#******************String split******************
print(str1.split('-'))
print(str1.split('-',3))  #split(regex,limit)
str1="expert at hello world"
print(str1.split(' ',3))  #split(regex,limit)
print(str1.split())



# ****************doc strings*****************
def printName(name):
	"""This function is used to print name"""
	print(name)

printName("omkar")
print(printName.__doc__)      #doc string
help(printName)               #it will print function name and doc string


# ***************string library********************
import string

#digits
print(string.digits)
print('9' in string.digits)

for i in '23423423s43209235':
	if(i not in string.digits):
		print("not a digit",i)

#letters
print(string.ascii_letters)
for i in 'akjsdf3hAKJD7FHJak3sdhf':
	if(i not in string.ascii_letters):
		print("not a letter",i)
		
#string.ascii_lowercase and string.ascii_uppercase:
