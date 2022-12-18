#!/usr/bin/env python3

calories = []
running_total = 0

# Open File
with open('01-calorie-counting - input', 'r') as input:
    for line in input:
        # A empty line (ie, just a new-line character) means move to next elf
        if line == "\n":
            calories = calories + [running_total]
            running_total = 0

        else:
            line_as_int = int(line.replace('\n',''))
            running_total = running_total + line_as_int

    # Catch for incase no blank line at end of file
    calories = calories + [running_total]
    
calories.sort(reverse=True)
print(f"Part 1:  {calories[0]}")

top_three = calories[0] + calories[1] + calories[2]
print(f"Part 2:  {top_three}")


