"""
2a. Write a generator function that takes a string as input and yields
all vowels from the phrase.
"""

def vowels_in_string(string):
    vowels = 'AEIOUaeiou'
    for char in string:
        if char in vowels:
            yield char

string = 'The quick brown fox jumps over the lazy dog'
for vowel in vowels_in_string(string):
    print(vowel)
