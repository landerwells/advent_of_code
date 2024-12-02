import os
from collections import defaultdict

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/1")

with open(file_path, "r") as file:
    input = file.read().strip().split("\n")

def part_one(input):
    list1 = []
    list2 = []

    for line in input:
        line = line.split()
        list1.append(int(line[0]))
        list2.append(int(line[1]))
        
    list1.sort()
    list2.sort()

    sum = 0
    for x, y in zip(list1, list2):
        sum += abs(x - y)


    print(sum)


def part_two(input):
    list1 = []

    defdict = defaultdict(int)

    for line in input:
        line = line.split()
        list1.append(int(line[0]))
        defdict[int(line[1])] += 1
        
    list1.sort()

    sum = 0

    for num in list1:

        sum += num * defdict[num]
    print(sum)




part_one(input)
part_two(input)
