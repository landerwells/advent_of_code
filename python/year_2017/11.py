with open("11.txt", "r") as file:
    input = file.read().strip().split(',')

q = 0
r = 0
s = 0

max_distance = 0

for dir in input:

    match dir:
        case "n":
            q += 0
            r += -1 
            s += 1
        case "ne":
            q += 1
            r += -1 
            s += 0
        case "se":
            q += 1
            r += 0
            s += -1
        case "s":
            q += 0
            r += 1
            s += -1
        case "sw":
            q += -1
            r += 1
            s += 0
        case "nw":
            q += -1
            r += 0
            s += 1

    max_distance = max(((abs(q) + abs(r) + abs(s)) // 2), max_distance)

print((abs(q) + abs(r) + abs(s))// 2)
print(max_distance)

