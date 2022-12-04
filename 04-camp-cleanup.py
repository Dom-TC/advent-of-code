#!/usr/bin/env python3

# Open File
fully_contained = 0
overlapped = 0
with open('04-camp-cleanup - input', 'r') as input:
    for line in input:
        line = line.replace('\n','')
        sections = line.split(',')

        elf_one = sections[0].split('-')
        elf_two = sections[1].split('-')

        elf_one_lower = int(elf_one[0])
        elf_one_higher = int(elf_one[1])
        elf_two_lower = int(elf_two[0])
        elf_two_higher = int(elf_two[1])

        if elf_one_lower <= elf_two_lower and elf_one_higher >= elf_two_higher:
            fully_contained = fully_contained + 1

        elif elf_two_lower <= elf_one_lower and elf_two_higher >= elf_one_higher:
            fully_contained = fully_contained + 1

        if elf_one_lower <= elf_two_lower and elf_one_higher >= elf_two_lower:
            overlapped = overlapped + 1
        elif elf_one_higher >= elf_two_higher and elf_one_lower <= elf_two_higher:
            overlapped = overlapped + 1
        elif elf_two_lower <= elf_one_lower and elf_two_higher >= elf_one_lower:
            overlapped = overlapped + 1
        elif elf_two_higher >= elf_one_higher and elf_two_lower <= elf_one_higher:
            overlapped = overlapped + 1


print(f"Part 1: {fully_contained}")
print(f"Part 2: {overlapped}")

