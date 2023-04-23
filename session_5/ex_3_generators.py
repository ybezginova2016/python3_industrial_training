"""
3. Write a generator function that takes a list of integers
as input and yields the cumulative sum of the integers in
the list.

For example, given the input [1, 2, 3], the generator
should yield 1, 3, and 6.
"""
# Option 1
def cum_sum(numbers):
    return [sum(numbers[:i+1]) for i in range(len(numbers))]

lst = [-184, 456, 184, 3]
print(cum_sum(lst))

"""
The code [sum(numbers[:i+1]) for i in range(len(numbers))] is a list comprehension that generates a new list by iterating over a range of indices of the numbers list and summing the elements up to and including that index.

Here's what each part of the code does:

= range(len(numbers)): generates a range of indices from 0 up to (but not including) the length of the numbers list.
= numbers[:i+1]: slices the numbers list up to and including the current index i, creating a new list containing the first i+1 elements of numbers.
= sum(numbers[:i+1]): calculates the sum of the new list created by the slice.
"""

# Option 2
def cumulative_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total

lst = [-184, 456, 184, 3]
for cumulative in cumulative_sum(lst):
    print(cumulative)
