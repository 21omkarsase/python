num_list=list(range(10,20,2)) #range(start,end-1,increment)
print(num_list)

# for loop
for i in range(2,51,3):
	if(i==50):
		print(i)
	else: 
		print(i,end=", ")
	
name_list=["Omkar","Sairaj","Rohan","Harsh","name1","name2"]
for name in name_list:
	if name=="Sairaj":
		continue
	print(name*2)
	if name=="Harsh":
		break		

#print  
for i in range(5):
   for j in range(i+1):
   		print(j+1,end=" ")
   print("\n")
		
# while loop
n=1
while (n<10):
	if n==3:
		n+=1
		continue
	print(n,end=" ")
	n+=1
	
	
