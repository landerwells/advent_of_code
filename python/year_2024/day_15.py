import os
from collections import defaultdict

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/15")

with open(file_path, "r") as file:
    input = file.read().strip()

# input = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

def parse(input):
    input = input.split("\n\n")
    grid = [list(line) for line in input[0].splitlines()]
    movements = list(input[1])

    return grid, movements

def part_one(input):
    grid, movements = parse(input)

    grid = process_moves(movements, grid)

    # Get the grid and the coordinates of all the O, and return the coords
    score = 0
    coords = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                coords.append((col, row))

    for x, y in coords:
        score += x + y * 100

    print(score)

def process_moves(movements, grid):
    for move in movements:

        # Find robot
        x = 0
        y = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "@":
                    x = col
                    y = row
        # for row in grid:
        #     print(row)
        # print(move)
        # print()

        # Get movement direction
        dx, dy = 0, 0
        match move:
            case "^":
                dx, dy = 0, -1
            case ">":
                dx, dy = 1, 0
            case "v":
                dx, dy = 0, 1
            case "<":
                dx, dy = -1, 0

        grid = move_robot(x, y, dx, dy, grid)
    return grid

def move_robot(x, y, dx, dy, grid):
    nx, ny = x + dx, y + dy
    if grid[ny][nx] == '.':
        grid[y][x], grid[ny][nx] = grid[ny][nx], grid[y][x]
    elif grid[ny][nx] == 'O':
        spaces = 0
        while grid[y + dy * spaces][x + dx * spaces] not in ['.', '#']:
            spaces += 1
        if grid[y + dy * spaces][x + dx * spaces] == '.':
            grid[y][x] = '.'
            grid[y + dy][x + dx] = '@'
            grid[y + dy * spaces][x + dx * spaces] = 'O'

    return grid

def part_two(input):
    # TODO: Implement part two solution
    pass

part_one(input)
part_two(input)
