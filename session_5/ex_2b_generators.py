"""
2b. Write a generator function that takes a string as input and yields
all the words in the string that starts with a vowel.
"""

def vowels_only(string):
    vowels = 'AEIOUaeiou'
    for word in string.split():
        if word[0] in vowels:
            yield word


string = 'Everybody has a chance!'
for word in vowels_only(string):
    print(word)
