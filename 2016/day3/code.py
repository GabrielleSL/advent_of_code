file = [sorted(list(map(int, filter(None, a.strip().split(" "))))) for a in open("input.txt", "r").readlines()]
file2 = [list(map(int, filter(None, a.strip().split(" ")))) for a in open("input.txt", "r").readlines()]

ans1 = 0
ans2 = 0

for a in file:
    if sum(a[:2]) > a[2]:
        ans1 += 1

for a in range(0, len(file2), 3):
    res1 = sorted([file2[a][0], file2[a+1][0], file2[a+2][0]])
    res2 = sorted([file2[a][1], file2[a+1][1], file2[a+2][1]])
    res3 = sorted([file2[a][2], file2[a+1][2], file2[a+2][2]])
    if sum(res1[:2]) > res1[2]:
        ans2 += 1
    if sum(res2[:2]) > res2[2]:
        ans2 += 1
    if sum(res3[:2]) > res3[2]:
        ans2 += 1

print("PART 1:", ans1)

print("PART 2:", ans2)

