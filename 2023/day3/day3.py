def part1():
    f = open("day1_input.txt", "r").readlines()
    sum = 0

    for l in range(0, len(f)):
        for k in range(0, len(f[l])):
            if f[l][k] in ['+', '-', '$', '#', '%', '&', '/', '*', '=', '@']:
                f, num = lookAroundSymbol(f, [l, k])
                sum += num

    print(sum)


def lookAroundSymbol(file, pos):
    sum = 0
    for i in range(max(0, pos[0] - 1), min(pos[0] + 2, len(file))):
        for j in range(max(0, pos[1] - 1), min(pos[1] + 2, len(file[0]))):
            if file[i][j].isdigit():
                file[i], num = getAdjNumber(file[i], j)
                sum += num

    return file, sum


def getAdjNumber(line, pos):
    num_start, num_end = pos, pos
    while True:
        if num_start < 0 or not line[num_start - 1].isdigit():
            break
        else:
            num_start -= 1
    while True:
        if num_end > len(line) or not line[num_end + 1].isdigit():
            break
        else:
            num_end += 1

    num = int(line[num_start:num_end + 1])

    for i in range(num_start, num_end + 1):
        line = line[:i] + "." + line[i + 1:]

    return line, num


def part2():
    f = open("day1_input.txt", "r").readlines()

    sum = 0

    for l in range(0, len(f)):
        for k in range(0, len(f[l])):
            if f[l][k] == "*":
                gear_power = lookAroundSymbolP2(f, [l, k])
                sum += gear_power

    print(sum)


def lookAroundSymbolP2(file, pos):
    nums = []
    for i in range(max(0, pos[0] - 1), min(pos[0] + 2, len(file))):
        for j in range(max(0, pos[1] - 1), min(pos[1] + 2, len(file[0]))):
            if file[i][j].isdigit():
                file[i], num = getAdjNumberP2(file[i], j)
                nums.append(num)

    if len(nums) == 2:
        return nums[0] * nums[1]
    return 0


def getAdjNumberP2(line, pos):
    num_start, num_end = pos, pos
    while True:
        if num_start < 0 or not line[num_start - 1].isdigit():
            break
        else:
            num_start -= 1
    while True:
        if num_end > len(line) or not line[num_end + 1].isdigit():
            break
        else:
            num_end += 1

    num = int(line[num_start:num_end + 1])

    for i in range(num_start, num_end + 1):
        line = line[:i] + "." + line[i + 1:]

    return line, num


# part1()
part2()
