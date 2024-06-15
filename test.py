class Test:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def getDetails(self):
        return {"name":self.__name, "age": self.__age}

test1 = Test("test1", 20)

print(test1.getDetails())
