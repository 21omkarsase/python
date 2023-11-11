# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"student created with name {self.name}"
#
# student1 = Student("Omkar", 20)
#
# print(student1.name)

class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"student created with name {self.name} and age {self.age}"

s1 = Student("John", 36)

print(s1.name, s1.age)
print(s1)