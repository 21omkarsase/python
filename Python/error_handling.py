a,b=2,4

try:
	print("resource open")
	print(c)
	print(a/b)
	k=int(input("Enter a number"))
	print(k)
	list1=[1,2,4]
	print(list1[3])
	
#IndentationError is raised at ""compile"" time. try-except can only handle exceptions that are raised at run time.
# except IndentationError as e:  
# 	print("Name error occured!",e)
# so indentation error will always stop the program
	
except NameError as e:
	import traceback
	print('d\n')
	traceback.print_exc()
	print("Name error occurred!",e)

except ZeroDivisionError as e: #throws ZeroDivisionError for b==0
	print("You can't divide a number by zero")

except ValueError as e:      #invalid input
	print("Invalid input",e)

except IndexError as e:  #accessing index out of range
	print("Index out of range",e)

except Exception as e:    #default error with err message
	print("Something went wrong...",e)
	
finally:    #this block will always execute
	print("resource close")