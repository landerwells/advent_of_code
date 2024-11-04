with open("09.txt", "r") as file:
    input = file.read().strip()

def part_one(input):
    i = 0
    is_trash = False
    stack = 0
    sum = 0

    while i < len(input):

        match input[i]:
            case "<":
                is_trash = True
            case ">":
                is_trash = False
            case "{":
                if not is_trash:
                    stack += 1
                    sum += stack
            case "}":
                if not is_trash:
                    stack -= 1
            case _:
                pass

        if input[i] == "!":
            i += 2
        else:
            i += 1

    print(sum)

def part_two(input):

    i = 0
    start_counting = False
    count = 0

    while i < len(input):

        match input[i]:
            case "<":
                if start_counting:
                    count += 1
                start_counting = True
            case ">":
                start_counting = False
            case "!":
                pass
            case _:
                if start_counting:
                    count += 1

        if input[i] == "!":
            i += 2
        else:
            i += 1


    print(count)

# part_two("<{o\"i!a,<{i<a>")
# part_two("<random characters>")
# part_one("{{<!!>},{<!!>},{<!!>},{<!!>}}")

part_one(input)
part_two(input)
