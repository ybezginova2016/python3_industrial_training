"""
TASK 1
Create a Dog class with the following attributes: name, breed, and age. The class should also have the following methods: bark() and info().
The bark() method should print "Woof!" to the console, and the info() method should print the dog's name, breed, and age
to the console in the format "Name: {name}, Breed: {breed}, Age: {age}".

"""

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("Woof!")

    def info(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}")

# Example usage
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog1.bark()  # Output: Woof!
dog1.info()  # Output: Name: Buddy, Breed: Golden Retriever, Age: 3

# option 2
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("Woof!")

    def info(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}")