class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # another method to use attribute calling from the constructor
        return f"{self.name}({self.age})"

    def printname(self):
        print(self.firstname, self.lastname)

    def myFunc(abc):
        print('Hello' + abc.name)

p1 = Person('John', 30)
print(p1.name)
print(p1.age)

print(Person)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        # Person.__init__(self, fname, lname)
        # self.height = height

x = Student('Mike', 'Olisen', 2019)
x.printname()