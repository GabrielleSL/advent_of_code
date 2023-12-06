def part1():
    f = open("input.txt", "r").readlines()

    seeds = list(map(int, f[0].strip().split(": ")[1].split(" ")))
    maps = []

    for line in f[2:]:
        if "map:" in line:
            maps.append([])
        elif line.strip() == "":
            continue
        else:
            maps[-1].append(list(map(int, line.strip().split(" "))))

    for m in maps:
        for s in range(len(seeds)):
            for l in m:
                if l[1] <= seeds[s] < l[1] + l[2]:
                    seeds[s] = l[0] + (seeds[s] - l[1])
                    break

    seeds.sort()
    print(seeds[0])


def part2():
    f = open("input.txt", "r").readlines()

    seeds = list(map(int, f[0].strip().split(": ")[1].split(" ")))
    ranges = []
    for s in range(0, len(seeds), 2):
        ranges.append([seeds[s], seeds[s] + seeds[s + 1] - 1])

    maps = []

    for line in f[2:]:
        if "map:" in line:
            maps.append([])
        elif line.strip() == "":
            continue
        else:
            maps[-1].append(list(map(int, line.strip().split(" "))))

    for m in maps:
        s = 0
        while s < len(ranges):
            for l in m:
                if l[1] <= ranges[s][0] < l[1] + l[2]:
                    ranges[s][0] = l[0] + (ranges[s][0] - l[1])
                    if ranges[s][1] >= l[1] + l[2]:
                        ranges.append([l[1] + l[2], ranges[s][1]])
                        ranges[s][1] = l[0] + l[2] - 1
                    else:
                        ranges[s][1] = l[0] + (ranges[s][1] - l[1])
                    break

            s += 1
        ranges = concat_ranges(ranges)


    min_loc = [i[0] for i in ranges]
    min_loc.sort()
    print(min_loc[0])

def concat_ranges(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    i = 0
    while i < len(ranges) - 1:
        if ranges[i][1] >= ranges[i + 1][0]:
            ranges[i] = [ranges[i][0], max(ranges[i + 1][1], ranges[i][1])]
            ranges.pop(i + 1)
        else:
            i += 1
    return ranges

# part1()
# print()
part2()
