"""
Find the average value of a specific key in a JSON file containing an
array of dictionaries:

Write a Python program that reads a JSON file containing an array
of dictionaries, calculates the average value of a specific key.
"""

import json

file = "/session_6_decor_json\\data.json"

with open(file, "r") as f:
    data = json.load(f)

print(json.dumps(data, indent=4))

def calculate_average(data, key):
    total = 0
    count = 0

    for d in data:
        if key in d:
            total += d[key]
            count += 1

    if count > 0:
        average = total / count
        print(f"The average {key} is {average}")
        return average
    else:
        print(f"No '{key}' values found in data")
        return None

average_score = calculate_average(data, "score")

# option 2
with open(file, 'r')as data:

    json_obj = json.load(data)
    for record in json_obj:
        record = dict(record)
    key = input("Get average of 'age' or 'score'? ")
    print(float(sum(rec[key] for rec in json_obj)/ len(json_obj)))