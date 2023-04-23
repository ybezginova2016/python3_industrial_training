# 2.Write a lambda function that takes a string as input and returns
# True if the string is a palindrome
# (i.e., reads the same forward and backward),
# and False otherwise.

is_palindrome = lambda s: s == s[::-1]

print(is_palindrome('1001'))
print(is_palindrome('hello'))
print(is_palindrome('HelleH'))

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('1001'))
print(is_palindrome('hello'))
print(is_palindrome('HelleH'))

is_palindrome = lambda s: all(s[i] == s[-i-1] for i in range(len(s)//2))
string = "HelleH"
result = is_palindrome(string)
print(result)