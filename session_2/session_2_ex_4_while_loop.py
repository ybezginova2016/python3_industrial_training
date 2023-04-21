"""
1. Write a program which repeatedly reads numbers until the
user enters `done`. Once `done` is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333

sum()
len()

from statistics import mean
mean()

"""

##### Solution 1
total = 0
count = 0

while True:
    number = input("Enter a number: ")
    if number == "done":
        break

    try:
        number = float(number)
    except ValueError:
        print("Invalid input")
        continue

    total += number
    count += 1

if count > 0:
    average = total / count
else:
    average = 0

print(total, count, average)


##### Solution 2
from statistics import mean

numbers = []

while True:
    number = input("Enter a number: ")
    if number == "done":
        break

    try:
        number = float(number)
    except ValueError:
        print("Invalid input")
        continue

    numbers.append(number)

total = sum(numbers)
count = len(numbers)

if count > 0:
    average = mean(numbers)
else:
    average = 0

print(total, count, average)

