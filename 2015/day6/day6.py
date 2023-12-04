def part1():
    f = open("day6_input.txt", "r")
    # f = [
    #     "toggle 0,0 through 999,999"
    # ]
    lights = [[0 for j in range(1000)] for i in range(1000)]

    for l in f:
        instructions = l.strip().split(" ")
        if instructions[0] == "turn":
            start = instructions[2].split(",")
            end = instructions[4].split(",")
            state = 0 if instructions[1] == "off" else 1
            for i in range(int(start[0]), int(end[0])+1):
                for j in range(int(start[1]), int(end[1])+1):
                    lights[i][j] = state

        elif instructions[0] == "toggle":
            start = instructions[1].split(",")
            end = instructions[3].split(",")
            for i in range(int(start[0]), int(end[0]) + 1):
                for j in range(int(start[1]), int(end[1]) + 1):
                    lights[i][j] = 0 if lights[i][j] == 1 else 1

    s = 0
    for i in range(0, len(lights)):
        s += sum(lights[i])
    print(s)

def part2():
    f = open("day6_input.txt", "r")
    lights = [[0 for j in range(1000)] for i in range(1000)]

    for l in f:
        instructions = l.strip().split(" ")
        if instructions[0] == "turn" and instructions[1] == "on":
            start = instructions[2].split(",")
            end = instructions[4].split(",")
            for i in range(int(start[0]), int(end[0])+1):
                for j in range(int(start[1]), int(end[1])+1):
                    lights[i][j] += 1

        elif instructions[0] == "turn" and instructions[1] == "off":
            start = instructions[2].split(",")
            end = instructions[4].split(",")
            for i in range(int(start[0]), int(end[0])+1):
                for j in range(int(start[1]), int(end[1])+1):
                    lights[i][j] = max(lights[i][j]-1, 0)

        elif instructions[0] == "toggle":
            start = instructions[1].split(",")
            end = instructions[3].split(",")
            for i in range(int(start[0]), int(end[0]) + 1):
                for j in range(int(start[1]), int(end[1]) + 1):
                    lights[i][j] += 2

    s = 0
    for i in range(0, len(lights)):
        s += sum(lights[i])
    print(s)

# part1()
part2()