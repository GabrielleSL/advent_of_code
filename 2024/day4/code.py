file = open("input.txt", "r").readlines()

ans1 = 0
ans2 = 0

grid = [list(a.strip()) for a in file]

rowL = len(grid)
colL = len(grid[0])

for a in range(rowL):
    for b in range(colL):
        # PART 1
        # check forward and back
        if b+3 < colL and ''.join(grid[a][b:b+4]) in ["XMAS", "SAMX"]:
            ans1 += 1
        # check up and down
        if a+3 < rowL and grid[a][b] + grid[a+1][b] + grid[a+2][b] + grid[a+3][b] in ["XMAS", "SAMX"]:
            ans1 += 1
        # check diagonal left to right
        if a+3 < rowL and b+3 < colL and grid[a][b] + grid[a+1][b+1] + grid[a+2][b+2] + grid[a+3][b+3] in ["XMAS", "SAMX"]:
            ans1 += 1
        # check diagonal right to left
        if a+3 < rowL and b-3 >= 0 and grid[a][b] + grid[a+1][b-1] + grid[a+2][b-2] + grid[a+3][b-3] in ["XMAS", "SAMX"]:
            ans1 += 1

        # PART 2
        if a+2 < rowL and b+2 < colL and grid[a][b] + grid[a+1][b+1] + grid[a+2][b+2] in ["MAS", "SAM"] and grid[a][b+2] + grid[a+1][b+1] + grid[a+2][b] in ["MAS", "SAM"]:
            ans2 += 1

print(ans1)
print(ans2)