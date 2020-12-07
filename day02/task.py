def solve():
    # Stores the input
    task_input = []

    # Getting input
    with open("day02/resources/input.txt") as input_file:
        lines = input_file.readlines()
        for line in lines:
            task_input.append(line)

    # Printing out the input
    print("Task Input: {}\n".format(task_input))

    # Stores the output
    output_t1 = 0
    output_t2 = 0

    # Checking how many passwords are valid
    for line in task_input:
        split = line.split(" ")
        lower, upper = split[0].split("-")
        c = split[1].replace(":", "")
        password = split[2]
        count = password.count(c)

        # Checks if valid in task 1
        if int(lower) <= count <= int(upper):
            output_t1 += 1

        # Checks if valid in task 2
        if (password[int(lower) - 1] == c) ^ (password[int(upper) - 1] == c):
            output_t2 += 1

    print("Output Task 1: {}".format(output_t1))
    print("Output Task 2: {}".format(output_t2))
