"""
2.Write a program to prompt for a score between 0.0 and
1.0. If the score is out of range, print an error message. If the score is
between 0.0 and 1.0, print a grade using the following table:

Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F

"""

score = float(input("Please insert your score: "))
if score >= 0.9:
    print("A")
elif score >=0.8 and score < 0.9:
    print("B")
elif score >= 0.7 and score < 0.8:
    print('C')
elif score >= 0.6 and score > 0.7:
    print("D")
else:
    print("F")

try:
    score = float(input("Please insert your score: "))
    if score < 0.0 or score > 1.0:
        raise ValueError("Score must be between 0.0 and 1.0")
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print("D")
    else:
        print("F")
except ValueError as e:
    print("Error:", e)


### Part 2

def calculate_grade(*args, **kwargs):
    try:
        score = float(kwargs['score'])
        if score < 0.0 or score > 1.0:
            raise ValueError("Score must be between 0.0 and 1.0")
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        else:
            return "F"
    except ValueError as e:
        return "Error: " + str(e)

score = input("Please insert your score: ")
grade = calculate_grade(score=score)
print(grade)

