print("2"=="2")
class Employee:
    no_of_leaves = 10
    pass


omkar = Employee()
omkar.name = "omkar"
omkar.college = "PCE"
omkar.age = 20

sairaj = Employee()
sairaj.name = "sairaj"
sairaj.college = "Terna"
sairaj.age = 20

print(sairaj.name)
print(1, sairaj.__dict__)
print(sairaj.no_of_leaves)
sairaj.no_of_leaves = 12
print(Employee.__dict__)
print(sairaj.__dict__)
print(omkar.__dict__)
Employee.no_of_leaves = 11
print(Employee.no_of_leaves)
print(omkar.no_of_leaves)
print(sairaj.no_of_leaves)
print(omkar==omkar)