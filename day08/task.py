import re
from math import floor, ceil


def solve():
    # Stores the input
    task_input = []

    # Getting input
    with open("day08/resources/input.txt") as input_file:
        lines = input_file.readlines()
        for line in lines:
            task_input.append(line.strip('\n'))

    # Printing out the input
    print("Task Input: {}\n".format(task_input))

    # Stores the output
    output_t1 = 0
    output_t2 = 0

    print("Output Task 1: {}".format(output_t1))
    print("Output Task 2: {}".format(output_t2))


