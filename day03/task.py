def solve():
    # Stores the input
    task_input = []

    # Getting input
    with open("day03/resources/input.txt") as input_file:
        lines = input_file.readlines()
        for line in lines:
            task_input.append(line.strip('\n'))

    # Printing out the input
    print("Task Input: {}\n".format(task_input))

    # Stores the output
    output_t1 = 0
    output_t2 = 1

    # All possible movements
    for coord_modifier in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:

        # Initial position of the sled
        current_x = current_y = 0

        # Counts obstacles in current path
        current_obstacle_count = 0

        # Sliding down
        while current_y < len(task_input):

            # Checking for obstacle
            if task_input[current_y][current_x % len(task_input[0])] == '#':
                current_obstacle_count += 1

            # Next position of the sled
            current_x += coord_modifier[0]
            current_y += coord_modifier[1]

        if coord_modifier == [3, 1]:
            output_t1 = current_obstacle_count

        # Multiplying the result
        output_t2 *= current_obstacle_count

    print("Output Task 1: {}".format(output_t1))
    print("Output Task 2: {}".format(output_t2))


