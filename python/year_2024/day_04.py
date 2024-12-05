import os
from collections import defaultdict

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/4")

with open(file_path, "r") as file:
    input = [list(line.strip()) for line in file]

def part_one(input):
    count_xmas(input)

def count_xmas(input):
    for row in input:
        for col in input[row]:
            if input[row][col] == 'X':
                # Check all directions
                # could make a direction enum or something
                


def part_two(input):
    # TODO: Implement part two solution
    pass

part_one(input)
part_two(input)
