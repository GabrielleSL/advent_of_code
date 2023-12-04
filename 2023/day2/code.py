def part1():
    f = open("input.txt", "r")
    g_sum = 0

    for game in f:
        rounds = game.strip().split(": ")[1].split("; ")
        game_id = int(game.split(":")[0].split(" ")[1])
        possible_game = True
        for r in rounds:
            cubes = r.split(", ")
            for c in cubes:
                b = c.split(" ")
                if (b[1] == "red" and int(b[0]) > 12) or (b[1] == "green" and int(b[0]) > 13) or (
                        b[1] == "blue" and int(b[0]) > 14):
                    possible_game = False
                    break

        if possible_game: g_sum += game_id

    print(g_sum)


def part2():
    f = open("input.txt", "r")
    p_sum = 0

    for game in f:
        rounds = game.strip().split(": ")[1].split("; ")
        rgb = [0, 0, 0]

        for r in rounds:
            cubes = r.split(", ")

            for c in cubes:
                b = c.split(" ")

                if b[1] == "red" and int(b[0]) > rgb[0]:
                    rgb[0] = int(b[0])
                if b[1] == "green" and int(b[0]) > rgb[1]:
                    rgb[1] = int(b[0])
                if b[1] == "blue" and int(b[0]) > rgb[2]:
                    rgb[2] = int(b[0])

        power = rgb[0] * rgb[1] * rgb[2]
        p_sum += power

    print(p_sum)


# part1()
part2()
