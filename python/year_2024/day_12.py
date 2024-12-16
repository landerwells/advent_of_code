import os
from collections import defaultdict
from enum import Enum

class Direction(Enum):
    NORTH = (0, 1)
    EAST = (1, 0)
    SOUTH = (0, -1)
    WEST = (-1, 0)

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/12")

with open(file_path, "r") as file:
    input = file.read()

def parse(input):
    # Convert input string into a 2D list
    return [list(line) for line in input.splitlines()]

global_visited = set()

def part_one(input):
    input = parse(input)
    sum = 0
    for row in range(len(input)):
        for col in range(len(input[0])):
            if (col, row) not in global_visited:
                sum += explore(col, row, input)

    print(sum)

def explore(col, row, input):
    local_visited = set()
    perimeter = 0
    stack = [(col, row)]
    
    # algorithm to find all 
    while stack:
        x, y = stack.pop()
        if (x, y) in local_visited:
            continue
        local_visited.add((x, y))
        global_visited.add((x, y))

        # for all edges around that are the same, add to stack
        for direction in Direction:
            dir_x, dir_y = direction.value
            if 0 <= x + dir_x < len(input[0]) and 0 <= y + dir_y < len(input):
                if input[y][x] == input[y + dir_y][x + dir_x]:
                    stack.append((x + dir_x, y + dir_y))

    for entry in local_visited:
        col, row = entry
        perimeter += 4 - count_neighbors(col, row, input)

    # multiple area and permimeter of every region
    area = len(local_visited)

    return area * perimeter


def count_neighbors(col, row, input):
    char = input[row][col]
    neighbors = 0

    for direction in Direction:
        x, y = direction.value

        # make sure we are checking in bounds
        if 0 <= col + x < len(input[0]) and 0 <= row + y < len(input):
            if input[row + y][col + x] == char:
                neighbors += 1

    return neighbors


def part_two(input):
    input = parse(input)
    sum = 0
    for row in range(len(input)):
        for col in range(len(input[0])):
            if (col, row) not in global_visited:
                sum += explore2(col, row, input)

    print(sum)

def explore2(col, row, input):
    local_visited = set()
    stack = [(col, row)]
    
    # algorithm to find all 
    while stack:
        x, y = stack.pop()
        if (x, y) in local_visited:
            continue
        local_visited.add((x, y))
        global_visited.add((x, y))

        # for all edges around that are the same, add to stack
        for direction in Direction:
            dir_x, dir_y = direction.value
            if 0 <= x + dir_x < len(input[0]) and 0 <= y + dir_y < len(input):
                if input[y][x] == input[y + dir_y][x + dir_x]:
                    stack.append((x + dir_x, y + dir_y))

    for entry in local_visited:
        col, row = entry
        
    area = len(local_visited)

    sides = count_sides(local_visited)

    return area * sides

def count_sides(coordinates):
    """
    Count the number of sides a shape has given its coordinates in a 2D grid.

    Args:
        coordinates: A set of (x, y) tuples representing the shape's cells.

    Returns:
        The number of sides of the shape.
    """
    sides = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, Right, Down, Left

    for x, y in coordinates:
        # Check each neighbor
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            # If the neighbor is not part of the shape, it's an exposed side
            if neighbor not in coordinates:
                sides += 1

    return sides


part_one(input)
global_visited.clear()
part_two(input)
