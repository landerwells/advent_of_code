from functools import reduce
from operator import xor

with open("10.txt", "r") as file:
    input = file.read().strip()

def part_one(input):
    lengths = [int(x) for x in input.split(",")]
    inc_list = list(range(0, 256))

    new_list = knot_hash(inc_list, 1, lengths, 0, 0)

    print(new_list[0] * new_list[1])

def part_two(input):
    lengths = [ord(c) for c in input]  # Convert input to ASCII values
    lengths.extend([17, 31, 73, 47, 23])  # Append standard suffix

    # Run the knot hash algorithm for 64 rounds
    sparse_hash = knot_hash(list(range(256)), 64, lengths, 0, 0)

    # Create the dense hash by XORing blocks of 16
    dense_hash = [reduce(xor, sparse_hash[i:i + 16]) for i in range(0, 256, 16)]
    
    # Convert each number in dense_hash to a 2-digit hex and join them
    hex_str = ''.join(f"{num:02x}" for num in dense_hash)
    print(hex_str)  # This is the Knot Hash result

def knot_hash(array, rounds, lengths, skip_size, current_position):

    for _ in range(rounds):
        for length in lengths:
            # Reverse the segment of the array
            sublist = [array[(current_position + i) % len(array)] for i in range(length)]
            sublist.reverse()
            for i in range(length):
                array[(current_position + i) % len(array)] = sublist[i]

            # Move the current position forward by length + skip size
            current_position = (current_position + length + skip_size) % len(array)
            # Increment the skip size
            skip_size += 1

    return array

part_one(input)
part_two(input)
