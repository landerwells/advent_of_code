import os
import re

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/13")

with open(file_path, "r") as file:
    input = file.read().strip()

def parse(input):
    input = input.split("\n\n")
    return input

def solve(input, offset):
    input = parse(input)
    sum = 0
    for game in input:
        nums = tuple(map(int, re.findall(r"\d+", game)))
        result = find_integer_intersection(nums, offset)

        if result is not None:
            sum += result[0] * 3 + result[1]
    print(sum)

def find_integer_intersection(nums, offset):
    a1, a2, b1, b2, c1, c2 = nums
    c1 += offset
    c2 += offset
    # Calculate the determinant
    determinant = a1 * b2 - a2 * b1
    
    # Check if lines are parallel
    if determinant == 0:
        return None
    
    # Calculate x and y
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    
    # Check if x and y are whole numbers
    if x.is_integer() and y.is_integer():
        return int(x), int(y)  # Return as integers
    else:
        return None

solve(input, 0)
solve(input, 10000000000000)
