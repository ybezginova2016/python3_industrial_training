from dataclasses import dataclass
from typing import List

@dataclass
class Person():
    name: str
    age: int
    height: float
    email: str

@dataclass
class People():
    people: List[Person]

joe = Person('Joe', 25, 1.85, 'joe@test.com')
mary = Person('Mary', 43, 1.67, 'mary@test.com')

print(People([joe, mary]))

