import re


def solve():

    # Storing all passports
    passports = []

    a = [[].append(line) for line in open("day04/resources/input.txt").readlines()]
    print(a)

    # Getting input
    with open("day04/resources/input.txt") as input_file:
        lines = input_file.readlines()

        # Stores the current passport
        current_passport = []

        for line in lines:
            if line == '\n':
                current_passport.sort()
                passports.append(''.join(current_passport))
                current_passport = []
            else:
                current_passport.extend(line.replace('\n', "").split(" "))

    print(sum(bool(re.match("^byr:(19[2-9][0-9]|200[0-2])(?:cid:[1-9][0-9]*)?ecl:(amb|blu|brn|gry|grn|hzl|oth)eyr:(202[0-9]|2030)hcl:#[a-f0-9]{6}hgt:(((1[5-8][0-9])|(19[0-3]))cm|((59)|(6[0-9])|(7[0-6]))in)iyr:20((1[0-9])|20)pid:[0-9]{9}$", passport)) for passport in passports))

