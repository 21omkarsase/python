from datetime import date

class Person:
    def __init__(self, name, dob_str):
        # Convert dob string to date object (assuming valid format)
        self.dob = date.fromisoformat(dob_str)
        self._name = name  # Use private variable for name

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        today = date.today()
        years = today.year - self.dob.year
        # Check if birthday has passed in the current year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            years -= 1
        return years
    
    @age.setter
    def age(self, value):
        raise AttributeError("Age cannot be set directly. It's calculated based on the date of birth.")

    @age.deleter
    def age(self):
        raise AttributeError("Age cannot be deleted. It's calculated based on the date of birth.")
    
# Example usage
person = Person("Alice", "1990-01-01")

print(person.name)  # Access name with getter
print(person.age)  # Access age with getter (calculated)

# Attempt to set age (setter raises an error)
# person.age = 30  # This will raise an AttributeError

# Attempt to delete age (deleter prints a message)
# del person.age  # Prints: Age property deleted...
