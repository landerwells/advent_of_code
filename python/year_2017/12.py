from collections import defaultdict

with open("12.txt", "r") as file:
    input = file.read().strip().split("\n")

def part_one(input):
    visited = set()
    pipes = parse(input)
    explore(0, pipes, visited)
    return len(visited)

def part_two(input):
    
    pipes = parse(input)

    groups = []
    for i in range(len(pipes)):
        visited = set()

        explore(i, pipes, visited)

        if sorted(visited) not in groups:
            groups.append(sorted(visited))

    return len(groups)



def parse(input):
    # construct all of the pipes
    pipes = defaultdict(list)
    for line in input:
        line = line.split()
        line.pop(1)
        line = list(map(lambda x: int(x.strip(",")), line))
        pipes[line[0]] = line[1:]
    
    return pipes

def explore(program, pipes, visited):
    visited.add(program)
    programs_to_explore = pipes[program]

    for pros in programs_to_explore:
        if pros not in visited:
            explore(pros, pipes, visited)


print(part_one(input))
print(part_two(input))

