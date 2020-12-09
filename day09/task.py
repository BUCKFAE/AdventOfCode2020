def solve():
    # Stores the input
    task_input = []

    # Getting input
    with open("day09/resources/input.txt") as input_file:
        lines = input_file.readlines()
        for line in lines:
            task_input.append(int(line.strip('\n')))

    # Printing out the input
    print("Task Input: {}\n".format(task_input))

    # Stores the output
    output_t1 = 0
    output_t2 = 0

    block_length = 25

    for current_number in range(block_length, len(task_input)):
        if check_if_valid(task_input[current_number - block_length:current_number], task_input[current_number]):
            pass
        else:
            output_t1 = task_input[current_number]

            possible_combinations = get_sub_lists(task_input)

            for combination in possible_combinations:
                if sum(combination) == task_input[current_number] and len(combination) >= 2:
                    output_t2 = min(combination) + max(combination)
                    break

            break

    print("Output Task 1: {}".format(output_t1))
    print("Output Task 2: {}".format(output_t2))


def check_if_valid(numbers, number):
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if numbers[i] != numbers[j] and numbers[i] + numbers[j] == number:
                return True
    return False


def get_sub_lists(numbers):
    for i in range(1, len(numbers) + 1):
        for j in range(len(numbers) - i + 1):
            yield numbers[j:j+i]


