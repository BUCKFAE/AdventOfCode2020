import re
from math import floor, ceil


def solve():

    # Stores the input
    groups = []

    # Getting input
    with open("day06/resources/input.txt") as input_file:
        lines = input_file.readlines()

        current_group = []

        for line in lines:
            if line.strip() == '':
                groups.append(current_group)
                current_group = []
            else:
                current_group.append(line.strip("\n"))

    # Printing out the input
    print("Task Input: {}\n".format(groups))

    # Stores the output
    output_t1 = 0
    output_t2 = 0

    for current_group in groups:
        output_t1 += len(set(''.join(c for c in current_group)))

        for c in current_group[0]:
            if all(c in m for m in current_group):
                output_t2 += 1

    print("Output Task 1: {}".format(output_t1))
    print("Output Task 2: {}".format(output_t2))


