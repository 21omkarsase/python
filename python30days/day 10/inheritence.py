class Vehicle:
    def __init__(self, type):
        self.type = type

class Car(Vehicle):
    def __init__(self, type, avgSpeed):
        super().__init__(type)

        self.speed = avgSpeed

    def printInfo(self):
        print("type : ", self.type)
        print("speed", self.speed)


c1 = Car("car", 60)

c1.printInfo()


# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Mixin classes
class JobInfoMixin:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary
    
    def job_info(self):
        return f"I work as a {self.job_title} and earn ${self.salary} per year."
        
    def greet(self):
        return f"Hello, my name is aasdf and I am 'sadf  years old."


class SkillsMixin:
    def __init__(self, skills):
        self.skills = skills
    
    def show_skills(self):
        return f"My skills include: {', '.join(self.skills)}."


# Child classes inheriting from Person and mixins
class Student(Person, SkillsMixin):
    def __init__(self, name, age, major, skills):
        Person.__init__(self, name, age)
        SkillsMixin.__init__(self, skills)
        self.major = major
    
    def greet(self):
        return super().greet() + f" I am studying {self.major}."

class Employee(Person, JobInfoMixin, SkillsMixin):
    def __init__(self, name, age, job_title, salary, skills):
        Person.__init__(self, name, age)
        JobInfoMixin.__init__(self, job_title, salary)
        SkillsMixin.__init__(self, skills)
    
    def greet(self):
        return JobInfoMixin.greet(self) + f" {super().job_info()}"

# Example usage
student = Student("Alice", 20, "Computer Science", ["Python", "Java", "SQL"])
employee = Employee("Bob", 30, "Software Engineer", 100000, ["C++", "JavaScript", "Django"])

print(student.greet())
print(student.show_skills())

print(employee.greet())
print(employee.show_skills())
