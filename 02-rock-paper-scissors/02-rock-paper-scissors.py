#!/usr/bin/env python3

score = 0
result_score = 0
shape_score = 0

winning_combos = ["AY", "BZ", "CX"]
drawing_combos = ["AX", "BY", "CZ"]

# Open File
with open('02-rock-paper-scissors - input', 'r') as input:
    for line in input:
        # Remove spaces and line breaks
        line = line.replace(' ', '').replace('\n', '')

        # Shape Score
        if line[1] == "X":
            shape_score = 1
        if line[1] == "Y":
            shape_score = 2
        if line[1] == "Z":
            shape_score = 3
            
        # Result Score
        if line in winning_combos:
            result_score = 6
        elif line in drawing_combos:
            result_score = 3
        else:
            result_score = 0

        score = score + shape_score + result_score    

print(f"Part 1: {score}")

score = 0
result_score = 0
shape_score = 0

produces_rock = ["AY", "BX", "CZ"]
produces_paper = ["AZ", "BY", "CX"]
produces_scissors = ["AX", "BZ", "CY"]

with open('02-rock-paper-scissors - input', 'r') as input:
    for line in input:
        # Remove spaces and line breaks
        line = line.replace(' ', '').replace('\n', '')

        # Shape Score
        if line in produces_rock:
            shape_score = 1
        if line in produces_paper:
            shape_score = 2
        if line in produces_scissors:
            shape_score = 3

        # Result Score
        if line[1] == "X":
            result_score = 0
        if line[1] == "Y":
            result_score = 3
        if line[1] == "Z":
            result_score = 6

        score = score + shape_score + result_score    

print(f"Part 2: {score}")
