import re
from math import floor, ceil


def solve():
    # Stores the input
    task_input = []

    # Getting input
    with open("day07/resources/input.txt") as input_file:
        lines = input_file.readlines()
        for line in lines:
            task_input.append(line.strip('\n'))

    # Printing out the input
    print("Task Input: {}\n".format(task_input))

    # Stores the output
    output_t1 = 0
    output_t2 = 0

    # Stores all bag rules
    bags = {}

    # Creating all bag rules
    for line in task_input:
        bag_color = ' '.join(line.split(" ")[0:2])
        containing = line.replace(bag_color + " bags contain ", "")

        inside_bag = []

        for contains in containing.split(", "):
            if contains != "no other bags.":
                inside_bag.append(contains.replace(".", ""))

        bags[bag_color] = inside_bag

    start_bag = "shiny gold"

    get_bag_combinations(bags, start_bag)

    # Getting all gold combinations
    bag_combinations = get_bag_combinations(bags, "shiny gold")
    print("Bags that can eventually contain a shiny gold one: {}".format(bag_combinations))

    output_t1 = len(bag_combinations)

    output_t2 = get_required_bag_count(bags, "shiny gold")

    print("Output Task 1: {}".format(output_t1))
    print("Output Task 2: {}".format(output_t2))


def get_required_bag_count(bags, bag):
    current_bag = bags[bag]

    output = 0

    if not current_bag:
        return 0

    for sub_bag in current_bag:
        amount = int(sub_bag.split(" ")[0])
        color = ' '.join(sub_bag.split(" ")[1:3])
        output += (get_required_bag_count(bags, color) * int(amount)) + amount

    return output


def get_bag_combinations(bags, bag):
    level_1_bags = get_bags_that_hold_bag(bags, bag)
    # print("Bag: {}\t LV 1: {}".format(bag, level_1_bags))

    # No Bags contain this bag -> returning nothing
    if not level_1_bags:
        return level_1_bags

    for current_bag in level_1_bags:
        current_lv_2_bags = get_bag_combinations(bags, current_bag)
        for current_lv_2_bag in current_lv_2_bags:
            if current_lv_2_bag not in level_1_bags:
                level_1_bags.append(current_lv_2_bag)

    # print("Bag: {}\t LV 2: {}".format(bag, level_1_bags))
    return level_1_bags


def get_bags_that_hold_bag(bags, bag):
    result = []

    for current_bag in bags:
        matching = [s for s in bags[current_bag] if bag in s]
        if matching:
            result.append(current_bag)
    return result
