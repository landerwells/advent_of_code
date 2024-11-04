import os
from collections import defaultdict

# Resolve the path to the input file
file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2017/8")

with open(file_path, "r") as file:
    input = file.read().strip().split("\n")


registers = defaultdict(int)

largest_ever = 0

for line in input:
    args = line.split()

    reg1 = args[0]
    inc_or_dec = args[1]
    value1 = int(args[2])
    reg2 = args[4]
    op = str(args[5])
    value2 = int(args[6])

    is_valid = False

    match op:
        case "==":
            if registers[reg2] == value2:
                is_valid = True
        case "!=":
            if registers[reg2] != value2:
                is_valid = True
        case ">":
            if registers[reg2] > value2:
                is_valid = True
        case "<":
            if registers[reg2] < value2:
                is_valid = True
        case ">=":
            if registers[reg2] >= value2:
                is_valid = True
        case "<=":
            if registers[reg2] <= value2:
                is_valid = True
        case _:
            print(op)
    
    
    if is_valid:
        if inc_or_dec == 'inc':
            registers[reg1] += value1
        else:
            registers[reg1] -= value1

    largest_ever = max(max(list(registers.values())), largest_ever)


largest = max(list(registers.values()))
print(largest)
print(largest_ever)



