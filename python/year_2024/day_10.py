import os
from enum import Enum

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/10")

class Direction(Enum):
    NORTH = (0, -1)  # Moving up decreases the row (y)
    EAST = (1, 0)    # Moving right increases the column (x)
    SOUTH = (0, 1)   # Moving down increases the row (y)
    WEST = (-1, 0)   # Moving left decreases the column (x)

with open(file_path, "r") as file:
    input = file.read()

def parse(input):
    return [[int(char) for char in line] for line in input.splitlines() if line.strip()]

def part_one(input):
    input = parse(input)
    score = 0

    # Find zeros.
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == 0:
                score += dfs(col, row, input)

    print(score)

def dfs(x, y, input):
    stack = [(x, y)]
    visited = set()
    score = 0

    while stack:
        col, row = stack.pop()
        if (col, row) in visited:
            continue
        visited.add((col, row))

        if input[row][col] == 9:
            score += 1
        looking_for = input[row][col] + 1

        for direction in Direction:
            dir_x, dir_y = direction.value
            if 0 <= row + dir_y < len(input) and 0 <= col + dir_x < len(input[row]):
                if input[row + dir_y][col + dir_x] == looking_for:
                    stack.append((col + dir_x, row + dir_y))
    return(score)

def dfs2(x, y, input):
    stack = [(x, y)]
    score = 0

    while stack:
        col, row = stack.pop()

        if input[row][col] == 9:
            score += 1
        looking_for = input[row][col] + 1

        for direction in Direction:
            dir_x, dir_y = direction.value
            if 0 <= row + dir_y < len(input) and 0 <= col + dir_x < len(input[row]):
                if input[row + dir_y][col + dir_x] == looking_for:
                    stack.append((col + dir_x, row + dir_y))
    return(score)


def part_two(input):
    input = parse(input)
    score = 0

    # Find zeros.
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == 0:
                score += dfs2(col, row, input)

    print(score)

part_one(input)
part_two(input)
