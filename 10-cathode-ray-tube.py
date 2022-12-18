#!/usr/bin/env python3

total = 0
x = 1
cycle = 1

display = []
current_row = ""

with open('10-cathode-ray-tube - input', 'r') as input:
    for line in input:
        if x <= cycle % 40 <= x + 2:
            current_row = current_row + "#"
        else:
            current_row = current_row + " "

        line = line.replace('\n','')

        cycle = cycle + 1

        if line.startswith('addx'):
            # Check multiplication in case middle of double addx command
            if cycle % 40 == 20:
                total = total + (cycle * x)
            elif cycle % 40 == 1:
                display.append(current_row)
                current_row = ""

            # Check display mid command
            if x <= cycle % 40 <= x + 2:
                current_row = current_row + "#"
            else:
                current_row = current_row + " "

            x = x + int(line[5:])
            cycle = cycle + 1

        if cycle % 40 == 20:
            total = total + (cycle * x)
        elif cycle % 40 == 1:
            display.append(current_row)
            current_row = ""

print(f"Part 1: {total}")
print()
print("Part 2:")
for row in display:
    print(row)


