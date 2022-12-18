#!/usr/bin/env python3

import re

is_preamble = True
has_defined_stacks = False
stacks = {}
with open('05-supply-stacks - input', 'r') as input:
    for line in input:
        if line == "\n":
            is_preamble = False 

        elif is_preamble == True:
            # Setup the stacks
            stack_index = 1
            stack_number = 0
            line_length = len(line)

            while stack_index < line_length:
                # On first line, create keys for each stack in stacks
                if has_defined_stacks == False:
                    stacks[stack_number] = []

                crate = line[stack_index]
                is_crate = re.match(r"\b[A-Z]\b", crate)
                if is_crate != None:
                    stacks[stack_number].append([crate])

                stack_index = stack_index + 4
                stack_number = stack_number + 1

            has_defined_stacks = True

        else:
            # Process the stacks
            line = line.replace('\n','').split(" ")

            crate_count = int(line[1])
            start_position = int(line[3]) - 1
            end_position = int(line[5]) - 1

            while crate_count > 0:
                crate_to_move = stacks[start_position][0]
                stacks[start_position].pop(0)
                stacks[end_position].insert(0, crate_to_move)

                crate_count = crate_count - 1

top_row = ""
index = 0
while index <= (stack_number - 1):
    top_row = top_row + str(stacks[index][0][0])
    index = index + 1

print(f"Part 1: {top_row}")



is_preamble = True
has_defined_stacks = False
stacks = {}
with open('05-supply-stacks - input', 'r') as input:
    for line in input:
        if line == "\n":
            is_preamble = False 

        elif is_preamble == True:
            # Setup the stacks
            stack_index = 1
            stack_number = 0
            line_length = len(line)

            while stack_index < line_length:
                # On first line, create keys for each stack in stacks
                if has_defined_stacks == False:
                    stacks[stack_number] = []

                crate = line[stack_index]
                is_crate = re.match(r"\b[A-Z]\b", crate)
                if is_crate != None:
                    stacks[stack_number].append([crate])

                stack_index = stack_index + 4
                stack_number = stack_number + 1

            has_defined_stacks = True

        else:
            # Process the stacks
            line = line.replace('\n','').split(" ")

            crate_count = int(line[1])
            start_position = int(line[3]) - 1
            end_position = int(line[5]) - 1

            temp_stack = []
            temp_crate_count = 0
            while crate_count > 0:
                crate_to_move = stacks[start_position][0]
                stacks[start_position].pop(0)
                temp_stack.insert(0, crate_to_move)

                crate_count = crate_count - 1
                temp_crate_count = temp_crate_count + 1

            while temp_crate_count > 0:
                crate_to_move = temp_stack[0]
                temp_stack.pop(0)
                stacks[end_position].insert(0, crate_to_move)

                temp_crate_count = temp_crate_count - 1


top_row = ""
index = 0
while index <= (stack_number - 1):
    top_row = top_row + str(stacks[index][0][0])
    index = index + 1

print(f"Part 2: {top_row}")

