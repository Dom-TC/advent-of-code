#!/usr/bin/env python3



grid = []
with open('08-treetop-tree-house - input', 'r') as input:
    for line in input:
        grid.append(line.replace('\n',''))

    # Set some useful variables...
    height = len(grid)
    width = len(grid[0])

    # Trees on the perimiter are always included.
    # -4 to remove the 4 corners which would otherwise be counted twice.
    visible = (height * 2) + (width * 2) - 4

    best_score = 0

    # Start at 1 and end at height-1 to avoid perimiter
    for row_index in range(1, height - 1):
        row = grid[row_index]

        # Start at 1 and end at width-1 to avoid perimiter
        for column_index in range(1, width - 1):
            tree = row[column_index]

            # Part 1...

            # Start true and change to false as otherwise need to AND heights of all trees.
            # If any single tree is too tall, is_visible = false.
            is_visible_north = True
            is_visible_east = True
            is_visible_south = True
            is_visible_west = True

            # North...
            for i in range(row_index - 1, -1, -1):
                if tree <= grid[i][column_index]:
                    is_visible_north = False

            # East...
            for other_trees in row[column_index + 1:]:
                if tree <= other_trees:
                    is_visible_east = False

            # South...
            for i in range(row_index + 1, height):
                if tree <= grid[i][column_index]:
                    is_visible_south = False

            # West...
            for other_trees in row[:column_index]:
                if tree <= other_trees:
                    is_visible_west = False

            if is_visible_north or is_visible_east or is_visible_south or is_visible_west:
                visible = visible + 1

            # Part 2...
            for north_index in range(row_index - 1, -1, -1):
                if grid[north_index][column_index] >= tree:
                    break

            for east_index in range(column_index + 1, width):
                if row[east_index] >= tree:
                    break

            for south_index in range(row_index + 1, height):
                if grid[south_index][column_index] >= tree:
                    break

            for west_index in range(column_index - 1, -1, -1):
                if row[west_index] >= tree:
                    break

            score = (row_index - north_index) * (east_index - column_index) * (south_index - row_index) * (column_index - west_index)
            
            if score > best_score:
                best_score = score

    print(f"Part 1: {visible}")
    print(f"Part 2: {best_score}")
