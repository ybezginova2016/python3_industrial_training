"""
Write a lambda function that takes a string of words separated
by spaces, and returns a new string with the words in reverse
order. For example, given the string "the quick brown fox",
the function should return "fox brown quick the".

"""
# wrong
# def reverse_words(s):
#     words = s.split()
#     reversed_words = words[::-1]
#     reversed_s = ' '.join(reversed_words)
#     return reversed_s
#
# print(reverse_words("hello"))

def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    reversed_s = ' '.join(reversed_words)
    return reversed_s[::-1]

print(reverse_words("hello"))

str1 = "ama böyle olmaz"
reverser = lambda string: " ".join(string.split()[::-1])
print(reverser(str1))

# lambda
reverse_words = lambda s: ' '.join(s.split()[::-1])
print(reverser(str1))

"""
How it works:

- s.split() splits the input string into a list of words, using the default whitespace separator.
- [::-1] slices the list in reverse order, creating a new list with the words in reverse order.
- ' '.join() joins the list of reversed words back into a string, using a space as the separator.
"""


