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
    output_t2 = 0

    # Getting the output of t1
    output_t1 = check_if_runs_endless(task_input)[0]

    # Fixing the program
    for current_set in range(0, len(task_input)):
        for change_id in [1, 2]:
            new_program = task_input.copy()

            current_instruction = task_input[current_set]

            if change_id == 1:
                if "jmp" in current_instruction:
                    new_instruction = current_instruction.replace("jmp", "nop")
                    new_program[current_set] = new_instruction
            elif change_id == 2:
                if "nop" in current_instruction:
                    new_instruction = current_instruction.replace("nop", "jmp")
                    new_program[current_set] = new_instruction

            # Getting the result
            result = check_if_runs_endless(new_program)

            if result[1] == len(new_program):
                output_t2 = result[0]

    print("Output Task 1: {}".format(output_t1))
    print("Output Task 2: {}".format(output_t2))


def check_if_runs_endless(program):

    accumulator = 0

    visited = []
    current = 0
    # Checking where the program terminates

    while current not in visited and current != len(program):

        # The current instruction
        instruction = program[current].split(" ")[0]

        # Storing what we've already seen
        visited.append(current)

        # Executing the instruction
        if instruction == "nop":
            pass
        elif instruction == "acc":
            accumulator += int(program[current].split(" ")[1])
        elif instruction == "jmp":
            current += int(program[current].split(" ")[1]) - 1

        current += 1

    return accumulator, current



