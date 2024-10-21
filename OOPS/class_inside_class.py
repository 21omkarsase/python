    # Grouping of two or more classes. Suppose you have two classes Car and Engine. Every Car needs an Engine. But, Engine won't be used without a Car. So, you make the Engine an inner class to the Car. It helps save code.

    # Hiding code is another use of Nested classes. You can hide the Nested classes from the outside world.

    # It's easy to understand the classes. Classes are closely related here. You don't have to search for the classes in the code. They are all together.


class Student:
	def __init__(self, name, lap_name):
		self.name = name
		self.lap = self.Laptop(lap_name)
		
	def show(self):
		print(self.name)
		self.lap.show()
	
	class Laptop:
		def __init__(self, lap_name):
			self.lap_name = lap_name
		
		def show(self):
			print(self.lap_name)


s1=Student("omkar","hp")

# lap_s1=Student.Laptop("dell")
# lap_s1.show()

s1.show()


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = self.Engine()

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

    class Engine:
        def start(self):
            print("Engine started")

        def stop(self):
            print("Engine stopped")

# Create a car instance
my_car = Car("Toyota", "Camry")

# Access methods of Car class
my_car.drive()

# Access methods of Engine class through Car class instance
my_car.engine.start()
