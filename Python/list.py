#*****************Lists are mutable*******************

faang=["Facebook","Amazon","Apple","Netflix","Google"]

faang[3]="Microsoft"   #update element
del faang[1]           #delete element
faang.remove("Microsoft")
# del faang            #delete list

print(faang[::-1])     #slicing work same as string

for i in range(len(faang)):
	if(i==len(faang)-1):
		print(faang[i])
		continue
	print(faang[i],end=" ")


# *****************List comprehension**************
nums=[x for x in range(10,21)]
odds=[x for x in range(1,50) if x&1]  #[expression loop condition]
squares=[x*x for x in range(11)]

print(nums)
print(odds)
print(squares)
print(squares[:])


#***************List Methods**********************
random_list=["omkar",20,"PCE"];

#insert and append
random_list.append("DSA")            #insert at end of the list
random_list.insert(3,"Development")  #insert at specific index

#sort
faang.sort()  #can only sort list of same data type
#reverse
faang.reverse()

#pop
random_list.pop(3)           # remove and return ele present at index 3 
#clear
# random_list.clear()

#index
print(faang.index("Apple"))  #returns index of given ele
#count
print(faang.count("Apple"))  #returns count of given ele

#copy
com=faang.copy()             # shallow copy of original string
print(com," com")

print(random_list)
print(faang)



#***************List Functions**********************
print(len(faang))
print(max(squares))
print(min(squares))
print(sum(squares))        

print(list("omkarsase"))   #returns list


#**************for loops************
for square in squares:
	if(square==100):
		print(square*square)
		continue
	print(square*square,end=" ")
	
	
#***************Multi Dimensional Lists**********************
primes=[[2,3,5,7],[11,13,17,19]]

for i in range(len(primes)):
	for j in range(len(primes[i])):
		print(primes[i][j],end=" ")
	print("\n")
	
print(primes[1][2])


#***************List input**********************
list1=[]
# n=int(input("Enter the size of list"))
# list1=list(map(int,input("Enter the integers elements:").strip().split()))[:n]

# for i in range(n):
# 	l=[]
# 	for j in range(n):
# 		ele=input()
# 		l.append(int(ele))
# 	list1.append(l)
# 	del l
# for i in range(0,n):
# 	val=int(input())
# 	list1.append(val)
# creating an empty list
lst = []

# number of elements as input
# n = int(input("Enter number of elements : "))

# # iterating till the range
# for i in range(0, n):
# 	ele = int(input())

# 	lst.append(ele) # adding the element
	
# print(lst)

	

# print("list is : ",list1)



#********************filter map  lambda & reduce************************
#filter
def getVowels(let):
	vowels=['a','e','i','o','u']
	return let in vowels

letters=['a','d','e','k','e','m','w','u']
vowels=filter(getVowels,letters)

print(vowels,type(vowels))
vowels=list(vowels)
print(type(vowels),vowels[0])
for v in vowels:
	print(v)

#map
def get_updated_nums(a,b):
	return a+b
	
nums=[1,2,3,4]
smun=[4,3,2,1]
updated_nums=map(get_updated_nums,nums,smun)
print(updated_nums,type(updated_nums))
updated_nums=list(updated_nums)
print(updated_nums,type(updated_nums))

#list of strings
days=['fri','sat','sun']
happy_days=list(map(list,days))
print(happy_days)

#lambda
lam_fun=lambda x:x*x
print(lam_fun(10))

getMax=lambda a,b:a if(a>b) else b
print(getMax(19,29))

tables=[lambda x=x:x*10 for x in range(1,11)]
for x in tables:
	print(x(),end=" ")   #list of lambda functions

# list sorting
List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
print(type(res))

#filter with lambda
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list=list(filter(lambda x:x&1,li))
adv_list=list(filter(lambda x:x>30 and x<65,li))

print(final_list)
print(adv_list)

#map with lambda
list1=list(map(lambda x:x*2,li))
print(list1)

animals = ['dog', 'cat', 'parrot', 'rabbit']
upper_animals=list(map(lambda x:x.upper(),animals))
print(upper_animals)

#reduce
from functools import reduce

list1=[4,2,6,23,3]
sum=reduce(lambda x,y:x+y,list1)
max=reduce(lambda x,y:x if(x>y) else y,list1)

print(sum)
print(max)