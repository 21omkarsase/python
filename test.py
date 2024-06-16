class Test:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

test1 = Test("test1", 20)

print(test1.get_name())
print(test1.get_age())