import os
from enum import Enum

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/4")

with open(file_path, "r") as file:
    input = [list(line.strip()) for line in file]

class Direction(Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    EAST = (1, 0)
    WEST = (-1, 0)
    NORTHEAST = (1, -1)
    NORTHWEST = (-1, -1)
    SOUTHEAST = (1, 1)
    SOUTHWEST = (-1, 1)

def part_one(input):
    count = 0
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == 'X':
                # Check all directions
                for dir in Direction:
                    x, y = dir.value  # dir.value is the tuple (x, y)
                    for i in range(1, 4):
                        col_index = col + y * i
                        row_index = row + x * i
                        # need to check first if out of bounds
                        if 0 <= row_index < len(input) and 0 <= col_index < len(input[row]):
                            current_letter = input[row_index][col_index]
                            if i == 1 and current_letter == 'M':
                                continue
                            elif i == 2 and current_letter == 'A':
                                continue
                            elif i == 3 and current_letter == 'S':
                                count += 1
                            else:
                                break
    print(count)

def part_two(input):
    # only looking for MAS X's in this one, so no need for all the directions.
    count = 0

    for row in range(1, len(input) - 1):
        for col in range(1, len(input[row]) - 1):
            if input[row][col] == 'A':
                if input[row + 1][col + 1] == 'M' and input[row + 1][col - 1] == 'M' and input[row - 1][col - 1] == 'S' and input[row - 1][col + 1] == 'S':
                    count += 1
                if input[row + 1][col + 1] == 'S' and input[row + 1][col - 1] == 'M' and input[row - 1][col - 1] == 'M' and input[row - 1][col + 1] == 'S':
                    count += 1
                if input[row + 1][col + 1] == 'S' and input[row + 1][col - 1] == 'S' and input[row - 1][col - 1] == 'M' and input[row - 1][col + 1] == 'M':
                    count += 1
                if input[row + 1][col + 1] == 'M' and input[row + 1][col - 1] == 'S' and input[row - 1][col - 1] == 'S' and input[row - 1][col + 1] == 'M':
                    count += 1


    print(count)



part_one(input)
part_two(input)
