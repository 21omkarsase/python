#creating set
nums={1,2,3,4,5,6,1,2,3,4,5}
print(nums,type(nums),len(nums))

#set typecasting
nums=set([1,2,3,4,5,6,1,2,3,4,5])
print(nums,type(nums),len(nums))

#adding ele to set
nums.add("ten")

print(nums)

#frozen set
frozen_set=frozenset(nums)
# frozen_set=frozenset([1,2,3,4])

# frozen_set.add("2")             #frozenset can't be modified
print(frozen_set,type(frozen_set))


#***********Methods for set****************
#union of sets

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}


print(people.union(vampires))
print(people | vampires | dracula)  #union using |

#intersection of sets
print({1,2,3,4,5}.intersection({2,4,5}))
print({1,2,3,4,5} & {1,2,3} & {2,3})

#difference in sets
print({1,2,3,4,5}.difference({2,4,5}))
print({1,2,3,4,5} - {1,2,3})

#clear
people.clear()

# **************operators in sets*************
print("Karan" in vampires)
print("Karan" not in vampires)

s1={1,2,3,4,5}
s2={3,4,5}

# Proper subset definition
 
# A proper subset of a set A is a subset of A that is not equal to A. In other words, if B is a proper subset of A, then all elements of B are in A but A contains at least one element that is not in B.

# Proper superset definition
 
# A proper superset of a set A is a superset of A that is not equal to A. In other words, if B is a proper superset of A, then all elements of A are in B but B contains at least one element that is not in A.

print(s1==s2)
print(s1!=s2)
print(s1<=s2)     #is s1 is subset of s2
print(s1<s2)      #is s1 is proper subset of s2
print(s1>=s2)     #is s1 is superset of s2
print(s1>s2)      #is s1 is proper superset of s2
print(s1^s2)      #the set of elements in precisely one of s1 or s2

