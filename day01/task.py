def solve():
    # Stores the input
    task_input = []

    # Getting input
    with open("day01/resources/input.txt") as input_file:
        lines = input_file.readlines()
        for line in lines:
            task_input.append(int(line))

    # Printing out the input
    print("Task Input: {}\n".format(task_input))

    # Stores the output
    output_t1 = []
    output_t2 = []

    ##########
    # Task 1 #
    ##########

    # Finding two numbers that add up to 2020
    for first_number in task_input:
        for second_number in task_input:
            if first_number + second_number == 2020:
                result = first_number * second_number
                if result not in output_t1:
                    output_t1.append(result)

    ##########
    # Task 2 #
    ##########

    # Finding three numbers that add up to 2020
    for first_number in task_input:
        for second_number in task_input:
            for third_number in task_input:
                if first_number + second_number + third_number == 2020:
                    result = first_number * second_number * third_number
                    if result not in output_t2:
                        output_t2.append(result)

    print("Output Task 1: {}".format(output_t1))
    print("Output Task 2: {}".format(output_t2))

