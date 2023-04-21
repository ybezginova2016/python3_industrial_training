"""
Samuel Henderson
08:29 PM
SH
regex can be pain
Serdar Gündoğdu
08:29 PM
SG
no pain no gain
Samuel Henderson
08:29 PM
SH
:(
Serdar Gündoğdu
to
Everyone
08:33 PM
SG
sometimes I confuse too :)
Samuel Henderson
to
Everyone
08:53 PM
SH
I think ^ is used only for the first word or the beginning of the line, while \b is anywhere in the line
thumbs up
1
Haryanto
to
Everyone
08:54 PM

okay
Arsalan Yahyazadeh
to
Everyone
08:54 PM

regex.py
5.1 KB
Arsalan Yahyazadeh
to
Everyone
08:54 PM

regex_cheat_sheet.md
2.3 KB
Samuel Henderson
to
Everyone
08:54 PM
SH
cool
melis öztürk
to
Everyone
08:54 PM

thanks
Arsalan Yahyazadeh
to
Everyone
08:59 PM

Write a Python script that reads a text file and finds all the phone numbers in it. However, the script should only match phone numbers that meet the following criteria:

    The phone number must be in the format of either (XXX) XXX-XXXX or XXX-XXX-XXXX, where X represents a digit.
    The phone number must not contain any letters, symbols, or whitespace.
    The phone number must not be a fake number, which means that the area code (the first 3 digits) cannot start with 0 or 1, and the next digit after the area code cannot be 9.

For example, the script should match phone numbers like (123) 456-7890 or 456-789-1234, but not phone numbers like 012-345-6789 or 123-456-7899.


John Smith
123 Main St
Los Angeles, CA 90001
(555) 555-1234

Mary Johnson
456 Oak Ave
San Francisco, CA 94110
555-555-5678

Tom Brown
789 Pine Rd
San Diego, CA 92101
(123) 456-7890

Jane Lee
101 Elm St
New York, NY 10001
212-555-1212

Fake Person
789 Fake St
Boston, MA 02101
(012) 345-6789

"""
numbers = []
def make_list(input_data):
    numbers.append(input_data)
    return numbers

make_list(7)
print(make_list(42))