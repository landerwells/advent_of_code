import os
from collections import defaultdict
import math

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/5")

with open(file_path, "r") as file:
    input = file.read().strip().split("\n\n")

def part_one(input):
    rules = input[0].split("\n")
    rules_dict = defaultdict(list)
    for rule in rules:
        rule = rule.split("|")
        rule = list(map(lambda x: int(x), rule))
        rules_dict[rule[0]].append(rule[1])

    updates = input[1].split("\n")
    updates = list(map(lambda x: x.split(","), updates))

    sum = 0
    for update in updates:
        update = list(map(lambda x: int(x), update))
        if is_correct(update, rules_dict):
            sum += update[math.ceil(len(update) / 2) - 1]

    print(sum)

def is_correct(update, rules_dict):
    for rules in rules_dict:
        if rules not in update:
            continue
        first = update.index(rules)
        for x in rules_dict[rules]:
            if x not in update:
                continue
            if update.index(x) < first:
                return False

    return True


def part_two(input):
    rules = input[0].split("\n")
    rules_dict = defaultdict(list)
    for rule in rules:
        rule = rule.split("|")
        rule = list(map(lambda x: int(x), rule))
        rules_dict[rule[0]].append(rule[1])

    updates = input[1].split("\n")
    updates = list(map(lambda x: x.split(","), updates))

    incorrect_updates = []
    sum = 0
    for update in updates:
        update = list(map(lambda x: int(x), update))
        if not is_correct(update, rules_dict):
            update = correct_update(update, rules_dict)
            sum += update[math.ceil(len(update) / 2) - 1]

    print(sum)


def correct_update(update, rules_dict):
    # I kind of what to know why this worked, originally I wanted to try something
    # really stupid, which was tryig
    while not is_correct(update, rules_dict):
        for i in range(len(update)):
            for j in range(i+1, len(update)):
                if update[i] in rules_dict[update[j]]:
                    update[j], update[i] = update[i], update[j]

    return(update)

part_one(input)
part_two(input)
