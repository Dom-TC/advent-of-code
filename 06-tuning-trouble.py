#!/usr/bin/env python3

with open('06-tuning-trouble - input', 'r') as input:
    for line in input:
        marker = []
        marker_index = 0
        for character in line:
            # Pre-seed with first 4 characters
            if marker_index <= 3:
                marker = marker + [character]
            else:
                duplicates = [character for character in marker if marker.count(character) > 1]

                if len(duplicates) == 0:
                    print(f"Part 1: {marker_index}")
                    break
                else:
                    marker = marker + [character]
                    marker.pop(0)

            marker_index = marker_index + 1

with open('06-tuning-trouble - input', 'r') as input:
    for line in input:
        marker = []
        marker_index = 0
        for character in line:
            # Pre-seed with first 14 characters
            if marker_index <= 13:
                marker = marker + [character]
            else:
                duplicates = [character for character in marker if marker.count(character) > 1]

                if len(duplicates) == 0:
                    print(f"Part 2: {marker_index}")
                    break
                else:
                    marker = marker + [character]
                    marker.pop(0)

            marker_index = marker_index + 1
