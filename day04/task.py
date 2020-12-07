import re


def solve():

    # Stores all passports
    passports = []

    # Stores the current passport
    current_passport = []

    # Getting input
    with open("day04/resources/input.txt") as input_file:
        lines = input_file.readlines()
        for line in lines:
            # Appending the current passport
            if line == '\n':
                current_passport.sort()
                passports.append(current_passport)
                current_passport = []
            else:
                current_passport.extend(line.replace("\n", "").split(" "))

    # Stores the output
    output_t1 = 0
    output_t2 = 0

    # required fields
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    # Validating all passports
    for passport in passports:

        # Counts how many required fields the passport contains
        passport_required_field_count_t1 = 0
        passport_required_field_count_t2 = 0

        # Checking if the passport contains all required fields
        for required_field in required_fields:
            for passport_field in passport:
                if passport_field.startswith(required_field):

                    passport_required_field_count_t1 += 1

                    # Getting the value
                    value = passport_field.split(":")[1].strip()

                    if required_field == "byr":
                        if 1920 <= int(value) <= 2002:
                            passport_required_field_count_t2 += 1
                    if required_field == "iyr":
                        if 2010 <= int(value) <= 2020:
                            passport_required_field_count_t2 += 1
                    if required_field == "eyr":
                        if 2020 <= int(value) <= 2030:
                            passport_required_field_count_t2 += 1
                    if required_field == "hgt":
                        if value.endswith("cm"):
                            value = value.replace("cm", "")
                            if 150 <= int(value) <= 193:
                                passport_required_field_count_t2 += 1
                        elif value.endswith("in"):
                            if 59 <= int(value.replace("in", "")) <= 76:
                                passport_required_field_count_t2 += 1
                    if required_field == "hcl":
                        if re.match("#[a-f0-9]{6}", value):
                            passport_required_field_count_t2 += 1
                    if required_field == "ecl":
                        if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                            passport_required_field_count_t2 += 1
                    if required_field == "pid":
                        if re.match("^[0-9]{9}$", value):
                            passport_required_field_count_t2 += 1

                    break

        if passport_required_field_count_t1 == len(required_fields):
            output_t1 += 1

        if passport_required_field_count_t2 == len(required_fields):
            output_t2 += 1
            print(passport)

    print("Output Task 1: {}".format(output_t1))
    print("Output Task 2: {}".format(output_t2))


