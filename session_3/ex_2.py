# TASK 2
"""
{'stephen.marquard@uct.ac.za': 2, 'louis@media.berkeley.edu': 3, 'zqian@umich.edu': 4, 'rjlowe@iupui.edu': 2, 'cwen@iupui.edu': 5, 'gsilver@umich.edu': 3, 'wagnermr@iupui.edu': 1, 'antranig@caret.cam.ac.uk': 1, 'gopal.ramasammycook@gmail.com': 1, 'david.horwitz@uct.ac.za': 4, 'ray@media.berkeley.edu': 1}
cwen@iupui.edu: 5

cwen@iupui.edu: 5 - the most frequent
"""
# option 1
try:
    f = open("C:\\Users\\HOME\\PycharmProjects\\django_upgrade\\python\\session_3\\mbox-short.txt")
except FileNotFoundError:
    print("File not found")
else:
    sender_count = {}

    for line in f:
        if line.startswith('From:'):
            sender = line.split()[1]
            sender_count[sender] = sender_count.get(sender, 0) + 1
    print(sender_count)
    print("cwen@iupui.edu:", sender_count.get('cwen@iupui.edu', 0))

    f.close()

    ### option 2
    try:
        f = open("C:\\Users\\HOME\\PycharmProjects\\django_upgrade\\python\\session_3\\mbox-short.txt")
        listEmail = f.readlines()
        dictEmails = {}

        for x in listEmail:
            x = x.strip()
            if "From: " in x:
                if x.replace("From: ", "") in dictEmails:
                    numb = int(dictEmails[(x.replace("From: ", ""))])
                    numb += 1
                    dictEmails[(x.replace("From: ", ""))] = str(numb)
                else:
                    dictEmails[(x.replace("From: ", ""))] = str(1)
        print(dictEmails)
        max = 0
        value = ""
        for x in dictEmails:
            if int(dictEmails[x]) > max:
                max = int(dictEmails[x])
                value = x
        print(value, max)
    except FileNotFoundError:
        print("File has not been found")

        # solution
        d = dict()
        fname = 'mbox-short.txt'
        fhand = open(fname)
        for line in fhand:
            words = line.split()
            if len(words) < 3 or words[0] != 'From':
                continue
            else:
                if words[1] not in d:
                    d[words[1]] = 1
                else:
                    d[words[1]] += 1

        print(d)

        max_value = max(d.values())
        key = max(d, key=d.get)
        print(key + ': ' + str(max_value))


