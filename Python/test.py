tables=[lambda x=x:x*10 for x in range(1,11)]

print(list(filter(lambda x : x*x,[1, 2, 3])))