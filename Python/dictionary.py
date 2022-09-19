dict1={1:"One",2:"Two",3:"Three"}
for d in dict1:
   print(d)
print(dict1)

data={"name":"Omkar","age":20,"college":"PCE","skills":["dsa","dev"]}
print(data,data["age"])

#list of tuples to dictionary
dict1=dict([(1,"One"),(2,"Two"),(1,[1,2,3,4]),(3,"Three")])   #keys cant't be repeated
print(dict1,type(dict1))

#nested dictionary
Dict = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
  
print(Dict)
print(Dict[3]['B'])   #accessing nested dic elements

#get()
print(Dict.get(2))

#********************Dictionary Methods**********************
dict2=Dict.copy()                    #copy
# dict2.clear()                      #clear
items_of_dic=list(dict2.items())     #list containing tuple of key-pair if we don't use list(....)
# items_of_dic=list(items_of_dic)[2][1]
keys_of_dict=list(dict2.keys())      #list containing tuple of key if we don't use list(....)
values_of_dict=list(dict2.values())  #list containing tuple of values if we don't use list(....) 
dict2.update({3:"hello world"})      #update item with key
dict2[3]="world hello"

print(dict2)
print(items_of_dic,type(items_of_dic))
print(keys_of_dict,type(keys_of_dict))
print(values_of_dict,type(values_of_dict))
print(dict2.pop(3))              #pops and returns specific value 
print(dict2.popitem())           #pops out last ele




#iterating in dictionaries
dict3={"name":"Omkar","age":20,"college":"PCE","skills":["dsa","dev"]}
for i in dict3:
   print(i,dict3[i])

for i in dict3.items():
   print(i)
   
for i in dict3.keys():
   print(i)
   
for i in dict3.values():
   print(i)