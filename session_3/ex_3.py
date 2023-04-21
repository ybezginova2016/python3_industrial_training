# TASK 3
"""
{'uct.ac.za': 6, 'media.berkeley.edu': 4, 'umich.edu': 7,
'iupui.edu': 8, 'caret.cam.ac.uk': 1, 'gmail.com': 1}

"""
try:
    f = open("C:\\Users\\HOME\\PycharmProjects\\django_upgrade\\python\\session_3\\mbox-short.txt")
except FileNotFoundError:
    print("File not found")
else:
    domain_count = {}
    for line in f:
        if line.startswith('From:'):
            email = line.split()[1]
            domain = email.split('@')[1]
            domain_count[domain] = domain_count.get(domain, 0) + 1

    print(domain_count)

    f.close()

# SOLUTION

"""
This code reads a file named 'mbox-short.txt' and creates a dictionary that maps email domains to the number of times they appear in the file. Here is what the code does in detail:

It creates an empty dictionary using the built-in dict() function and assigns it to the variable d.

It opens the file named 'mbox-short.txt' using the built-in open() function and assigns it to the variable fhand.

It loops through each line of the file using a for loop, where line is a variable that holds each line of the file.

It splits each line into a list of words using the built-in split() function and assigns it to the variable words.

If the number of words in the line is less than 3 or the first word is not 'From', it skips the current iteration of the loop and goes to the next line.

If the line passes the previous condition, it extracts the second word of the line (which is the email address) and then extracts the email domain from it by splitting the email address at the '@' symbol and taking the second part of the resulting list.

It then updates the dictionary d by adding the extracted email domain as a key and incrementing its value by 1 using the built-in get() function to retrieve the value associated with the email domain key, and adding 1 to it.

Finally, after processing all the lines in the file, it prints the resulting dictionary d.
"""
d = dict()
fname = 'mbox-short.txt'
fhand = open(fname)
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From': continue
    else:
        line = words[1]
        words = line.split("@")[1]
        d[words] = d.get(words, 0) + 1
print(d)