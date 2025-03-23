import os

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/6")

with open(file_path, "r") as file:
    input = file.read().strip()

def parse(input):
    return [list(line) for line in input.splitlines()]

def part_one(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '^':
                starting_coord = []


def part_two(input):
    # TODO: Implement part two solution
    pass

part_one(input)
part_two(input)
