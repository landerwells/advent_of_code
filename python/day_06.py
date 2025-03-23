import os
from enum import Enum

# input = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2024/6")

with open(file_path, "r") as file:
    input = file.read()

def parse(input):
    # Convert input string into a 2D list
    return [list(line) for line in input.splitlines()]

# I think in some cases people use imaginary numbers in order to get the directions
# because they are capable of handling what comes on the coordinate plane
class Direction(Enum):
    NORTH = (0, -1)  # Moving up decreases the row (y)
    EAST = (1, 0)    # Moving right increases the column (x)
    SOUTH = (0, 1)   # Moving down increases the row (y)
    WEST = (-1, 0)   # Moving left decreases the column (x)

    def next(self):
        members = list(Direction)
        index = (members.index(self) + 1) % len(members)  # Loop around
        return members[index]

def part_one(input):
    input = parse(input)  # Parse the input into a 2D list
    coord_set = set()
    x, y = 0, 0

    # Find the starting position '^'
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == '^':
                x = col
                y = row
                break

    # Call move_guard to process the path
    move_guard(x, y, coord_set, input)
    print(len(coord_set))  # Output the number of unique coordinates visited

def move_guard(x, y, coord_set, input):
    direction = Direction.NORTH  # Start facing north

    while 0 <= y < len(input) and 0 <= x < len(input[0]):  # Ensure position is in bounds
        coord_set.add((x, y))  # Add the current position to the visited set
        next_x = x + direction.value[0]
        next_y = y + direction.value[1]

        # Handle out-of-bounds or obstacle case
        if next_x not in range(len(input[0])) or next_y not in range(len(input)):
            break  # Stop moving if out of bounds
        if input[next_y][next_x] == '.' or input[next_y][next_x] == '^':
            x, y = move(x, y, direction)
        else:
            # Turn to the next direction if blocked
            direction = direction.next()
            x, y = move(x, y, direction)

def move(x, y, direction):
    x = x + direction.value[0]
    y = y + direction.value[1]
    return (x, y)

def detect_infinite_loop(x, y, input):
    visited_set = set()
    direction = Direction.NORTH  # Start facing north

    while 0 <= y < len(input) and 0 <= x < len(input[0]):  # Ensure position is in bounds
        if (x, y, direction) in visited_set:
            return True

        visited_set.add((x, y, direction))  # Add the current position to the visited set
        next_x = x + direction.value[0]
        next_y = y + direction.value[1]

        # Handle out-of-bounds or obstacle case
        if next_x not in range(len(input[0])) or next_y not in range(len(input)):
            return False
        if input[next_y][next_x] == '.' or input[next_y][next_x] == '^':
            x, y = move(x, y, direction)
        else:
            # Turn to the next direction if blocked
            direction = direction.next()
            x, y = move(x, y, direction)

def part_two(input):
    sum = 0
    input = parse(input)
    x, y = 0, 0

    # Find the starting position '^'
    for row in range(len(input)):
        for col in range(len(input[row])):
            if input[row][col] == '^':
                x = col
                y = row
                break

    # for every variant of the input with one version of the row/col being
    # a #, find how many cause the guard to enter an infinite loop

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '.':
                input[i][j] = "#"

                if detect_infinite_loop(x, y, input):
                    sum += 1

                input[i][j] = "."
    print(sum)

part_one(input)
part_two(input)
