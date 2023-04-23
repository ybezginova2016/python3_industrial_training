"""
1. Write a lambda function that takes two lists of integers and
returns a new list with the maximum value for each index of
the two lists.

For example, given [1, 3, 5] and [2, 4, 6],
the function should return [2, 4, 6].
"""
#########option 1############
def max_index(lst1, lst2):
    return [max(x, y) for x, y in zip(lst1, lst2)]

#########option 2############
max_index = lambda lst1, lst2: [max(x, y) for x, y in zip(lst1, lst2)]

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]

result = max_index(lst1, lst2)
print(result)

result = max_index(lst1, lst2)
print(result)



