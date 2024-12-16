import os
from collections import Counter

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/11")

with open(file_path, "r") as file:
    input = file.read()

def parse(input):
    return [int(num) for num in input.split()]

def solve(blinks, input):
    input = parse(input)
    input = Counter(input)

    for _ in range(blinks):
        input = blink2(input)

    return sum(input.values())

def blink2(input):
    new_stones = Counter()
    for stone, amt in input.items():
        if stone == 0:
            new_stones[1] += amt
        elif len(str(stone)) % 2 == 0:
            l = len(str(stone))
            new_stones[int(str(stone)[:l // 2])] += amt
            new_stones[int(str(stone)[l // 2:])] += amt
        else:
            new_stones[stone * 2024] += amt
    return new_stones

# def blink(input):
#     new_input = []
#
#     for num in input:
#         if num == 0:
#
#             new_input.append(1)
#         elif len(str(num)) % 2 == 0:
#             power = pow(10, len(str(num)) // 2)
#             left_num = num // power
#             right_num = num % power
#             new_input.extend([left_num, right_num])
#         else:
#             new = num * 2024
#             # cache[num] = [new]
#             new_input.append(new)
#
#     return(new_input)

print(solve(25, input))
print(solve(75, input))
