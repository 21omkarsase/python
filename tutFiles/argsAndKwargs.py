# def fun(a,b,c):
#     print(a,b,c)
# fun(3,4)

def funArg(normal, *args, **kwargs):  # pass first normal arguments then args and then kwargs
    print(type(args))
    print(type(kwargs))
    print(normal)
    for item in args:
        print(item, end=" ")
    print()
    for key, value in kwargs.items():
        print(key, " : ", value)


sgra = [4, 2, 6, 7, 72]
sgrawk = {"name": "omkar", "college": "PCE", "age": 20, "Location": "Mumbai"}
funArg(45, *sgra, **sgrawk)
