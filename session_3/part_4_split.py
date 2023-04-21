from re import split

print(split('\d', 'On 12th Jan 2016, at 11:02 AM'))

"""
This code imports the split function from the Python re (regular expression) module and uses it to split a string based on the occurrence of digits in the string. Here is what the code does in detail:

The code imports the split function from the re module using the from ... import syntax.

The code then calls the split() function, passing two arguments: a regular expression string '\d' and the string 'On 12th Jan 2016, at 11:02 AM'.

The regular expression '\d' matches any digit (0-9) in the string.

The split() function splits the string 'On 12th Jan 2016, at 11:02 AM' at every occurrence of a digit and returns a list of substrings. In this case, the returned list will be ['On ', 'th Jan ', ', at ', ':', ' AM'].

The code then prints the resulting list using the built-in print() function.

So, the output of the code will be a list of substrings, where each substring is separated by a digit in the original string.
"""