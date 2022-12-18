#!/usr/bin/env python3

rope = [(0,0)] * 10
delta = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
seen_part1 = {(0, 0)}
seen_part2 = {(0, 0)}

def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1

with open('09-rope-bridge - input', 'r') as input:
    for line in input:
        direction, steps = line.split()
        steps = int(steps)

        for i in range(steps):
            head_x, head_y = rope[0]
            dx, dy = delta[direction]

            rope[0] = head_x + dx, head_y + dy

            for j in range(9):
                # Move each piece pair of rope pieces as head / tails pair
                head_x, head_y = rope[j]
                tail_x, tail_y = rope[j + 1]

                dx, dy = head_x - tail_x, head_y - tail_y
                
                if dx**2 + dy**2 > 2:
                    tail_x = tail_x + sign(dx)
                    tail_y = tail_y + sign(dy)
                    rope[j + 1] = (tail_x, tail_y)

            seen_part1.add(rope[1])
            seen_part2.add(rope[9])

    
    part_1 = len(seen_part1)
    part_2 = len(seen_part2)
    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")
