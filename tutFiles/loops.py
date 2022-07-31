def demoFun():
    """this is a demo function"""
    print("demo function")


print(demoFun.__doc__)
demoFun()
l = [["omkar", 1], ["sairaj", 2], ["rohan", 3]]
print(l)
l = ("omkar", 10), ("sairaj", 20), ("rohan", 30)
print(l)
for items, nos in l:
    print(items, " has ", nos)

dict1 = dict(l)
print(dict1)
print(dict1.items())
print(dict1.values())
print(dict1.keys)
for items, values in dict1.items():
    print(items, " --> ", values)

# short hand if else
a = int(input("a "))
b = int(input("b : "))
print("a>b") if a > b else print("b>a")
