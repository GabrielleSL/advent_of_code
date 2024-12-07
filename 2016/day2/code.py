from operator import add

directions = {
    'U': (-1,  0),
    'R': ( 0,  1),
    'D': ( 1,  0),
    'L': ( 0, -1),
}

keypad1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
keypad2 = [
        ["X", "X", "1", "X", "X"],
        ["X", "2", "3", "4", "X"],
        ["5", "6", "7", "8", "9"],
        ["X", "A", "B", "C", "X"],
        ["X", "X", "D", "X", "X"]]

file = [list(a.strip()) for a in open("input.txt", "r").readlines()]

ans1 = ""
ans2 = ""

position1 = [1, 1]
position2 = [2, 0]

for a in file:
    for b in a:
        new_position1 = list(map(add, position1, directions[b]))
        new_position2 = list(map(add, position2, directions[b]))

        if 0 <= new_position1[0] <= 2 and 0 <= new_position1[1] <= 2:
            position1 = new_position1

        if 0 <= new_position2[0] <= 4 and 0 <= new_position2[1] <= 4 and keypad2[new_position2[0]][new_position2[1]] != 'X':
            position2 = new_position2


    ans1 += str(keypad1[position1[0]][position1[1]])
    ans2 += str(keypad2[position2[0]][position2[1]])


print("PART 1:", ans1)

print("PART 2:", ans2)

