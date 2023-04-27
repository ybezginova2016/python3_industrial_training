"""
1. Write a Python program that reads a text file and prints the number of lines, words, and characters in the file.
"""

text_file = "C:\\Users\HOME\\PycharmProjects\\python3_industrial_training\\session_4_classes\\assignment_4\\file_handling.txt"

# 'r' in the open() function stands for "read mode". It is used
# to open a file for reading only. This means that you cannot
# modify the contents of the file when it is opened in read mode.
with open(text_file, 'r') as f:
    lines = 0
    words = 0
    characters = 0

    for line in f:
        lines += 1
        words += len(line.split())
        characters += len(line.strip())

print(f"Number of lines: {lines}")
print(f"Number of words: {words}")
print(f"Number of characters: {characters}")
print()
# write a function

def count_file_stats(filename):
    with open(filename, 'r') as f:
        lines = 0
        words = 0
        characters = 0
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)
    print(f"Number of lines: {lines}")
    print(f"Number of words: {words}")
    print(f"Number of characters: {characters}")

count_file_stats(text_file)

"""
The difference between characters += len(line.strip()) and characters += len(line) 
is that the former counts the number of characters in a line after removing any 
leading or trailing whitespace characters, while the latter counts 
the number of characters in a line without removing any whitespace characters.
"""

"""
2. Write a Python program that reads a CSV file and converts it into a dictionary. Each row of the CSV file should be
a key-value pair in the dictionary.
"""
import pandas as pd
taxi_file = "C:\\Users\\HOME\\PycharmProjects\\python3_industrial_training\\session_4_classes\\assignment_4\\taxi.csv"
taxi = pd.read_csv(taxi_file)
print(taxi)

# converting to dictionary
result = taxi.to_dict(orient='records')
print(result)

# without pandas
import csv

with open(taxi_file, 'r') as f:
    reader = csv.reader(f)
    # Extract header row and remaining rows
    header = next(reader)
    rows = list(reader)

# Convert rows to dictionary
result = {}
for row in rows:
    key = row[0]
    values = row[1:]
    result[key] = values

print(result)

"""
3. Write a Python program that reads a binary file and converts it into a hexadecimal string. 
The program should output the hexadecimal string to a text file.
"""
# Hello Arsalan! Could you please advise where I can get the binary file?

"""
4. Write a Python program that reads a text file containing numbers 
and calculates the sum of all the numbers in the file.
"""
# We take the same text file with this assignment
with open(text_file, 'r') as f:
    numbers = []
    for line in f:
        try:
            numbers.append(float(line.strip()))
        except ValueError:
            pass

sum_of_numbers = sum(numbers)
print(f"The sum of all the numbers in the file is {sum_of_numbers}.")

"""
5. Write a Python program that reads a text file and 
removes all the blank lines.
The modified text should be written back to the file.
"""
with open(text_file, 'r') as f:
    lines = f.readlines()

# Remove blank lines
lines = [line for line in lines if line.strip()]

with open('text_file.txt', 'w') as f:
    f.writelines(lines)
