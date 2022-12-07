#!/usr/bin/env python3

from collections import defaultdict

# Finalised file structure = {path: contents}
def build_file_system(lines):
    # Using defaultdict so don't need to worry about path already existing
    # can just use file_system[current_path].append()
    file_system = defaultdict(list)
    path = () 

    for line in lines:
        line = line.replace('\n','')

        split_line = line.split(" ")

        # We can ignore all lines starting with dir and $ ls
        # as only the file size is needed and we have to cd into a folder to get it's contents
        if split_line[0] == "$" and split_line[1] == "cd":
            if split_line[2] == '..':
                # Discard last path component to go up one level
                path = path[:-1]
            else:
                # Calculate path of the directory we are moving into
                new_path = path + (split_line[2],) # Needs to be a tuple to avoid TypeError when calculating new path

                # Add path to current directory
                file_system[path].append(new_path)

                path = new_path
        elif split_line[0].isdigit():
            size = split_line[0]
            file_system[path].append(int(size))

    return file_system


def calculate_directory_size(file_system, path):
    size = 0

    for component in file_system[path]:

        # component will either be a digit (ie file size) or a tuple (ie directory)
        if isinstance(component, int):
            # is file...
            size = size + component
        else:
            # Directory, recursively calculate size
            size = size + calculate_directory_size(file_system, component)

    return size

with open('07-no-space-left-on-device - input', 'r') as input:
    file_system = build_file_system(input)

    total = 0

    total_space = 70000000
    minimum_space_needed = 30000000
    current_space_available = total_space - calculate_directory_size(file_system, ("/",))
    additional_space_required = minimum_space_needed - current_space_available
    file_size_to_be_removed = total_space

    for path in file_system:
        size = calculate_directory_size(file_system, path)

        # For part 1...
        if size <= 100000:
            total = total + size

        # For part 2...
        if size >= additional_space_required:
            if size < file_size_to_be_removed:
                file_size_to_be_removed = size
        
    print(f"Part 1: {total}")
    print(f"Part 2: {file_size_to_be_removed}")
