"""
1. Write a generator function that takes a list of numbers as
input and yields only the even numbers.
"""

# nums = int(input('Enter the list of numbers: '))

def return_even(numbers):

    for num in numbers:
        if num % 2 == 0:
            yield num
    return 1

numbers = [6, 12, 111, 13, 0, -188]

for num in return_even(numbers):
    print(num)