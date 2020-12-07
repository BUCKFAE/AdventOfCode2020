import re
from math import floor, ceil


def solve():

    # Stores the input
    task_input = []

    # Getting input
    with open("day05/resources/input.txt") as input_file:
        lines = input_file.readlines()
        for line in lines:
            task_input.append(line.strip('\n'))

    # Printing out the input
    print("Task Input: {}\n".format(task_input))

    # Stores the output
    output_t1 = 0
    output_t2 = 0

    # Stores all rows of the plane
    rows = []

    # Filling rows
    for current_row_id in range(0, 127):
        rows.append([0] * 8)

    for current_seat in task_input:

        # Current upper and lower bound
        lower = 0
        upper = 127

        # Narrowing it down
        for current_row_instruction in current_seat[:7]:
            if current_row_instruction == "F":
                upper = floor((upper + lower) / 2)
            elif current_row_instruction == "B":
                lower = ceil((upper + lower) / 2)

        # Getting the correct row
        row = int(lower) if current_seat[7] == "F" else int(upper)

        lower = 0
        upper = 7

        # Narrowing it down
        for current_row_instruction in current_seat[7:10]:
            if current_row_instruction == "L":
                upper = floor((upper + lower) / 2)
            elif current_row_instruction == "R":
                lower = ceil((upper + lower) / 2)

        # Getting the correct col
        col = int(lower) if current_seat[9] == "L" else int(upper)

        # Seat-ID
        seat_id = (row * 8) + col

        if seat_id > output_t1:
            output_t1 = seat_id

        # There is someone on this seat
        rows[row][col] = 1

    # Finding the empty row
    for row_id in range(0, len(rows)):
        if rows[row_id].count(0) == 1:
            print(rows[row_id])
            output_t2 = row_id * 8 + rows[row_id].index(0)

    print("Output Task 1: {}".format(output_t1))
    print("Output Task 2: {}".format(output_t2))


