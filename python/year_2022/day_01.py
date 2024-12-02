import os
# from collections import defaultdict

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2022/1")

with open(file_path, "r") as file:
    input = file.read().strip().split("\n\n")

def elves(input):
    elves = []

    # input = map(lambda x: int(x.split("\n")), input)
    for elf in input:
        elf = elf.split("\n")
        elf = list(map(lambda x: int(x), elf))
        elves.append(sum(elf))

    return elves


def part_one(input):
    # TODO: Implement part one solution
    elves_list = elves(input)
    elves_list.sort()

    print(elves_list[-1])

def part_two(input):
    # TODO: Implement part two solution
    elves_list = elves(input)
    elves_list.sort()

    print(sum((elves_list[:3])))

part_one(input)
part_two(input)
