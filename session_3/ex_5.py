import re

text = "Here are some URLs: https://www.google.com, http://www.python.org, https://en.wikipedia.org/wiki/Python_(programming_language)"

urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

print(urls)


import re

text = "Here are some URLs: https://www.google.com, http://www.python.org, https://en.wikipedia.org/wiki/Python_(programming_language)"

urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

print(urls)