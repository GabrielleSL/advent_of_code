import re


def part1():
    f = open("day5_input.txt", "r")
    nice = 0

    for line in f:
        # condition 1: contains at least 3 vowels
        if len(re.findall("a|e|i|o|u", line)) < 3:
            continue

        # condition 2: contains at least one instance of a letter in a row
        for char in range(0, len(line) - 1):
            if line[char] == line[char + 1]:
                break
        else:  # doesn't execute if break out of for loop
            continue

        # condition 3: doesn't contain ab, cd, pq or xy
        if len(re.findall("ab|cd|pq|xy", line)) > 0:
            continue

        nice += 1

    print(nice)


def part2():
    f = open("day5_input.txt", "r")
    nice = 0

    for line in f:
        pairs = []
        con1 = False
        con2 = False

        # condition 1: has at least one pair that repeats without overlapping
        for c in range(0, len(line) - 1):
            pairs.append(f"{line[c]}{line[c + 1]}")

        for p in range(0, len(pairs) - 1):
            check_pair = pairs.pop(0)
            if check_pair in pairs[1:]:
                con1 = True
                break

        for c in range(0, len(line) - 2):
            if line[c] == line[c+2]:
                con2 = True
                break

        if con1 and con2: nice += 1

    print(nice)


# part1()
part2()
