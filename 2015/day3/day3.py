def part1():
    f = open("day3_input.txt", "r").readline()
    lat = 0  # <>
    lon = 0  # ^v
    visited = {"0,0"}
    for mov in f:
        if mov == ">": lat += 1
        elif mov == "<": lat -= 1
        elif mov == "^": lon += 1
        elif mov == "v": lon -= 1

        visited.add(f"{lat},{lon}")

    print(len(visited))

def part2():
    f = open("day3_input.txt", "r").readline()
    santa_pos = [0, 0]  # [lat, lon]
    robo_santa_pos = [0, 0]  # [lat, lon]
    visited = {"0,0"}  # set
    santa = True

    for mov in f:
        if santa:
            if mov == ">": santa_pos[0] += 1
            elif mov == "<": santa_pos[0] -= 1
            elif mov == "^": santa_pos[1] += 1
            elif mov == "v": santa_pos[1] -= 1
            visited.add(f"{santa_pos[0]},{santa_pos[1]}")
        else:
            if mov == ">": robo_santa_pos[0] += 1
            elif mov == "<": robo_santa_pos[0] -= 1
            elif mov == "^": robo_santa_pos[1] += 1
            elif mov == "v": robo_santa_pos[1] -= 1
            visited.add(f"{robo_santa_pos[0]},{robo_santa_pos[1]}")

        # alternate who moves
        santa = not santa

    print(len(visited))

# part1()
part2()