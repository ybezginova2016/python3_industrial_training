f = open("C:\\Users\\HOME\\PycharmProjects\\django_upgrade\\python\\session_3\\mbox-short.txt")

print(f.readline())
print(f.read())

"""
Sender: stephen.marquard@uct.ac.za
Sender: louis@media.berkeley.edu
Sender: zqian@umich.edu
Sender: rjlowe@iupui.edu
Sender: zqian@umich.edu
Sender: rjlowe@iupui.edu
Sender: cwen@iupui.edu
Sender: cwen@iupui.edu
Sender: gsilver@umich.edu
Sender: gsilver@umich.edu
Sender: zqian@umich.edu
Sender: gsilver@umich.edu
Sender: wagnermr@iupui.edu
Sender: zqian@umich.edu
Sender: antranig@caret.cam.ac.uk
Sender: gopal.ramasammycook@gmail.com
Sender: david.horwitz@uct.ac.za
Sender: david.horwitz@uct.ac.za
Sender: david.horwitz@uct.ac.za
Sender: david.horwitz@uct.ac.za
Sender: stephen.marquard@uct.ac.za
Sender: louis@media.berkeley.edu
Sender: louis@media.berkeley.edu
Sender: ray@media.berkeley.edu
Sender: cwen@iupui.edu
Sender: cwen@iupui.edu
Sender: cwen@iupui.edu
Total number of lines: 27
"""

count = 0
for line in f:
    if line.startswith('From:'):
        count += 1
        print("Sender:", line.strip())
print("Total number of emails:", count)

"""
This code opens the file "mbox-short.txt", loops over each line 
in the file, and checks if the line starts with the string "From:". 
If it does, it increments the email count and prints out the sender
in the desired format. Finally, it prints the total number of emails 
that were found.

In the context of the code I provided earlier, line.strip() is used to remove any leading or trailing whitespace characters (such as spaces, tabs, or newlines) from the line of text that was read from the file.

The strip() method in Python is a string method that returns a copy of the string with leading and trailing whitespace removed. This is often useful when processing text data from files or user input, as it helps to ensure that the text is properly formatted and free from any unwanted whitespace characters.

In the case of the code I provided, using line.strip() ensures that any extraneous whitespace characters are removed from the "From:" line before printing out the sender in the desired format.
"""

# option 2
try:
    f = open("C:\\Users\\HOME\\PycharmProjects\\django_upgrade\\python\\session_3\\mbox-short.txt")
except FileNotFoundError:
    print("File not found")
else:
    count = 0
    for line in f:
        if line.startswith('From:'):
            count += 1
            print("Sender:", line.strip())
    print("Total number of emails:", count)
    f.close()

# TASK 2
"""
{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3, 'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5, 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}
cwen@iupui.edu: 5
"""

# solution
filename = "mbox-short.txt"
try:
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            if line.startswith("From "):
                words = line.split()
                print("Sender:", words[1])
                count += 1
        print("Total number of lines:", count)
except FileNotFoundError:
    print("File not found")
