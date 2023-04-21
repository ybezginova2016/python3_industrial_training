# RegEx finds some patterns in the matches you have.
# https://xmind.works/share/vPw1ZTAh

import re

txt = 'The rain in Spain'

x = re.findall('ai', txt) # finding for 'ai' pattern
y = re.search('ai', txt) # looking for the 1st match

print(x)
print(y) # <re.Match object; span=(5, 7), match='ai'> 7 is not included

s = 'This is a demo'
match = re.search('demo', s)
print(match.start())
print(match.end()) # 14 is not included


###################
m = 'Hi. Hi again'

# without \
match2 = re.search(r'.', m)
print(match2)

# using \
match3 = re.search(r'\.', m)
print(match3)

# \d is equivlalent to [0-9]
p = re.compile('\d')
print(p.findall('I went to him at 11 a. m. on the 4th July 1886'))

txt = 'The rain in Spain'
x = re.split('ai', txt)
print(x)
# ['The r', 'n in Sp', 'n']

p = re.compile('-*\d+')
print(p.findall('I went to him at -11 a. m. on 4th July 1886'))


