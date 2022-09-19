# *****************Immutable*****************
sub=("ML","DCN",10,"MIP","PCE","SEAT","FWM")
print(sub)

#indexing, slicing and iterating same as strings
for s in sub:
	print(s,end=" ")
	
# **************functions********************
nums=(0,1,2,3,4,5,6,7,8,9)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(tuple([1,2,3,4]))

print(nums+sub)             #tuple concatenation
print((nums,sub,nums+sub))  #multi tuples
print(("pce",)*3)           #repetition tuples

