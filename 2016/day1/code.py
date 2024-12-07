directions = {
# dir, x, y, L, R
    'N': (-1,  0, 'W', 'E'),
    'E': ( 0,  1, 'N', 'S'),
    'S': ( 1,  0, 'E', 'W'),
    'W': ( 0, -1, 'S', 'N'),
}

file = open("input.txt", "r").readline().split(', ')

ans1 = 0
ans2 = 0

curr_dir = 'N'
position = [0, 0]

visited = [[0, 0]]

for a in file:
    curr_dir = directions[curr_dir][2 if a[0] == 'L' else 3]
    for b in range(int(a[1:])):
        position = [position[0] + directions[curr_dir][0], position[1] + directions[curr_dir][1]]

        if position in visited and ans2 == 0:
            ans2 = abs(position[0]) + abs(position[1])
        elif ans2 == 0:
            visited.append(position.copy())

ans1 = abs(position[0]) + abs(position[1])

print("PART 1:", ans1)

print("PART 2:", ans2)

