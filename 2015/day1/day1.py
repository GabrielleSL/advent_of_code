def part1():
    f = open("day1_input.txt", "r")

    floor = 0

    for par in f.readline():
        if par == "(":
            floor += 1
        elif par == ")":
            floor -= 1

    print(floor)


def part2():
    f = open("day1_input.txt", "r")

    floor = 0
    position = 0

    for par in f.readline():
        position += 1

        if par == "(":
            floor += 1
        elif par == ")":
            floor -= 1

        if floor < 0:
            break

    print(position)


# part1()
part2()
