import os
import heapq
# from collections import defaultdict

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/16")

input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

# with open(file_path, "r") as file:
#     input = file.read().strip()

def parse(input):
    return [list(line) for line in input.splitlines()]

def part_one(input):
    input = parse(input)
    score = 0

    end_coords = (0,0)
    start_coords = (0,0)

    for row in range(len(input)):
        for col in range(len(input[row])):
            current_char = input[row][col]
            if current_char == 'S':
                start_coords = (col, row)
            elif current_char == 'E':
                end_coords = (col, row)

    score = dijkstras(start_coords, end_coords, 1000, input)

    print(score)

def dijkstras(start, end, turn_cost, grid):




def part_two(input):
    # TODO: Implement part two solution
    pass

part_one(input)
part_two(input)
