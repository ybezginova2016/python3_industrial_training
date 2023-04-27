"""
Write a Python program that reads a JSON file containing a list
of numbers, finds the maximum and minimum values, and prints
them to the console.
"""
import json

file = "/session_6_decor_json\\number.json"

with open(file, 'r') as f:
    numbers = json.load(f)

print(json.dumps(numbers, indent=4))

min_num = min(numbers)
max_num = max(numbers)

print(f"Maximum value is {max_num} and minimum value is {min_num}")