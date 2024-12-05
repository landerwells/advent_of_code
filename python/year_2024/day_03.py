import os
from collections import defaultdict
import re

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/3")

with open(file_path, "r") as file:
    input = file.read().strip()

def part_one(input):
    # Find all occurrences of mul(number, number)
    mul = re.findall(r'mul\(\d+,\d+\)', input)

    total = 0
    for entry in mul:
        # Extract the two numbers using a regex with capture groups
        match = re.search(r'mul\((\d+),(\d+)\)', entry)
        if match:
            arg1, arg2 = match.groups()  # Get the two arguments as strings
            total += int(arg1) * int(arg2)

    print(total)



def part_two(input):
    pattern = r"don't\(\).*?do\(\)"
    
    # Use re.sub to replace the matched pattern with an empty string
    input = re.sub(pattern, "", input, flags=re.DOTALL)

    mul = re.findall(r'mul\(\d+,\d+\)', input)

    total = 0
    for entry in mul:
        # Extract the two numbers using a regex with capture groups
        match = re.search(r'mul\((\d+),(\d+)\)', entry)
        if match:
            arg1, arg2 = match.groups()  # Get the two arguments as strings
            total += int(arg1) * int(arg2)

    print(total)


part_one(input)
part_two(input)
