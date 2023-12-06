def part1():
    time_list = [35, 93, 73, 66]
    dist_list = [212, 2060, 1201, 1044]

    ways_to_beat = 1

    for r in range(len(time_list)):
        times = 0

        for hold_time in range(time_list[r]):
            if (time_list[r] - hold_time) * hold_time > dist_list[r]:
                times += 1

        ways_to_beat *= times

    print(ways_to_beat)


def part2():
    time_mil = 35937366
    dist_mil = 212206012011044

    times = 0
    for hold_time in range(time_mil):
        if (time_mil - hold_time) * hold_time > dist_mil:
            times += 1

    print(times)


part1()
part2()
