class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        if self.fname == None or self.lname == None:
            return f"Employee name is not set please set it using setter"
        return f"Employee name is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return f"Employee name is not set please set it using setter"
        return f"{self.lname}{self.fname}@gamil.com"

    @email.setter
    def email(self, string):
        self.fname = string.split("@")[0].split(".")[1]
        self.lname = string.split("@")[0].split(".")[0]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


e1 = Employee("omkar", "sase")
e2 = Employee("sairaj", "lakde")
print(e2.explain())
print(e2.email)
e2.lname = "ambani"
print(e2.email)
e2.email = "kadam.rohan@gmail.com"
print(f"Employee 2 name is {e2.fname} {e2.lname}")
del e2.email
print(e2.email)
