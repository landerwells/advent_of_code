import os

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/2")
with open(file_path, "r") as file:
    input = file.read().strip().split("\n")

def part_one(input):
    print(solve(input, False))

def part_two(input):
    print(solve(input, True))

def solve(input, part_two):
    count = 0

    for line in input:
        line = list(map(int, line.split()))

        if is_safe(line, part_two):
            count += 1

    return count

def is_safe(line, part_two):
    if line == sorted(line):
        if least_one_most_three(line):
            return True

    if line == sorted(line)[::-1]:
        if least_one_most_three(line[::-1]):
            return True

    if part_two:
        for i in range(len(line)):
        # Exclude the element at index `i`
            temp = line[:i] + line[i+1:]

            if temp == sorted(temp):
                if least_one_most_three(temp):
                    return True

            if temp == sorted(temp)[::-1]:
                if least_one_most_three(temp[::-1]):
                    return True

    return False

def least_one_most_three(line):
    nums = []
    for i in range(len(line) - 1):
        pair = (line[i], line[i + 1])
        nums.append(pair[1] - pair[0])

    for i in nums:
        if i < 1 or i > 3:
            return False

    return True

part_one(input)
part_two(input)
