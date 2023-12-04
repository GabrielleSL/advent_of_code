import re


def part1():
    f = open("input.txt", "r")
    sum = 0

    for line in f:
        fal = getNumber(line)
        sum += fal

    print(sum)


def getNumber(str):
    nums = []
    for c in str:
        if c.isdigit():
            nums.append(c)
    return int(f"{nums[0]}{nums[-1]}")


def part2():
    f = open("input.txt", "r")
    sum = 0

    for line in f:
        fal = getNumber(replaceWordWithNum(line))
        sum += fal

    print(sum)


def replaceWordWithNum(str):
    mapping = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
               "nine": "9"}
    new_str = str
    for k in mapping:
        ind = [m.start() for m in re.finditer(k, str)]
        for i in ind:
            new_str = new_str[:i] + mapping.get(k) + new_str[i + 1:]
    return new_str


# part1()
part2()
