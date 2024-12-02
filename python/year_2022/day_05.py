import os

file_path = os.path.expanduser("~/.cache/advent_of_code_inputs/2022/5")

with open(file_path, "r") as file:
    input = file.read().split("\n\n")

def parse_grid(input):
    grid = []
    string = input[0].split("\n")

    for row in range(len(string) - 1, -1, -1):
        temp = []
        for col in range(len(string[row])):
            if col % 4 == 1:
                temp.append(string[row][col])
        if row != len(string) - 1:
            grid.append(temp)

    grid = [list(x) for x in zip(*grid)]
    final_grid = []

    for row in range(len(grid)):
        temp = []
        for col in range(len(grid[row])):
            if grid[row][col].isalpha():
                temp.append(grid[row][col])
        final_grid.append(temp)
        print(temp)

    return final_grid

def parse_directions(input):
    return input[1].strip().split("\n")

def apply_directions(grid, directions):

    for dir in directions:
        dir = dir.split(" ")
        num_crates_to_move = int(dir[1])
        from_stack = int(dir[3]) - 1
        to_stack = int(dir[-1]) - 1

        temp = []
        for _ in range(num_crates_to_move):
            temp.append(grid[from_stack].pop())
            # grid[to_stack].append(grid[from_stack].pop())
        temp.reverse()
        grid[to_stack].extend(temp)

def top_crates(grid):
    string = ""
    for row in grid:
        string += row[-1]

    return string
    
def part_one(input):
    # first we are going to want to parse the input into directions and grid
    grid = parse_grid(input)
    directions = parse_directions(input)

    apply_directions(grid, directions)
    print(top_crates(grid))


def part_two(input):
    # TODO: Implement part two solution
    pass

part_one(input)
part_two(input)
