class MyClass:
    static_variable = 10  # Class variable

    @classmethod
    def access_static_variable(cls):
        return cls.static_variable

    @staticmethod
    def static_method():
        return MyClass.static_variable  # Accessing the class variable directly

# Accessing the class variable through the class method
result1 = MyClass.access_static_variable()

# Accessing the class variable through the static method
result2 = MyClass.static_method()

print(result1)  # Output: 10
print(result2)  # Output: 10