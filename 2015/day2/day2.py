def part1():
    f = open("day2_input.txt", "r")
    total = 0

    for box in f:
        dim = sorted([int(num) for num in box.split("x")])
        surface = 2*dim[0]*dim[1] + 2*dim[0]*dim[2] + 2*dim[1]*dim[2] + dim[0]*dim[1]
        total += surface

    print(total)

def part2():
    f = open("day2_input.txt", "r")
    total = 0

    for box in f:
        dim = sorted([int(num) for num in box.split("x")])
        ribbon_len = 2*dim[0] + 2*dim[1] + dim[0]*dim[1]*dim[2]
        total += ribbon_len

    print(total)



# part1()
part2()