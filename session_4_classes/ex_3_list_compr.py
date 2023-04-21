"""
1. Write a list comprehension to find all the numbers between 1
and 1000 that are divisible by 7 but not by 5.
"""
numbers = []

for i in range(1, 1001):
    if i % 7 == 0 and i % 5 != 0:
        numbers.append(i)

print(numbers)

numbers = [i for i in range(1, 1001) if i % 7 == 0 and i % 5 != 0]
print(numbers)

### TASK 2 ###
# 2. Write a list comprehension to find all the prime numbers
# between 1 and 100.

prime_numbers = []

for n in range(2, 101):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        prime_numbers.append(n)

print(prime_numbers)

# list comprehension
prime_numbers = [n for n in range(2, 101) if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))]
print(prime_numbers)
