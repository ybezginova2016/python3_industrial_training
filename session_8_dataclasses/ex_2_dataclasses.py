"""
Create a dataclass called Student with the following attributes:
name (str), id (int), grades (list of floats). Write a method called
average_grade that returns the average of the student's grades.
Instantiate an object of Student with a name of "Alice", id of 12345,
and grades of [3.5, 4.0, 3.7], and print out their average grade.
"""

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    id: int
    grades: list[float]

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


# create a Student object and print their average grade
alice = Student("Alice", 12345, [3.5, 4.0, 3.7])
print(alice.average_grade())
