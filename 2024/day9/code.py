disk_map = [a.strip() for a in open("input.txt", "r").readlines()][0]

ans1 = 0
ans2 = 0

# PART 1
file = True
index = 0
disk_block = []
for a in disk_map:
    if file:
        for b in range(int(a)):
            disk_block.append(f"{index}")
        index += 1
    else:
        disk_block += ("."*int(a))
    file = not file


for a in range(len(disk_block)-1, 0, -1):
    if disk_block[a] != '.':
        try:
            new_index = disk_block.index('.', 0, a)
            disk_block[new_index], disk_block[a] = disk_block[a], disk_block[new_index]
        except:
            break

for a in range(len(disk_block)):
    if disk_block[a] == '.':
        break
    ans1 += a * int(disk_block[a])



# PART 2
def to_str(tp):
    new_str = ""
    for a in tp:
        if a[0] == '.':
            new_str += '.' * a[1]
        else:
            new_str += ''.join(b for b in a)
    return new_str

file = True
index = 0
disk_block_2 = []
for a in disk_map:
    if file:
        f = []
        for b in range(int(a)):
            f.append(f"{index}")
        disk_block_2.append(f)
        index += 1
    else:
        disk_block_2.append([".", int(a)])
    file = not file

for a in range(len(disk_block_2)-1, 0, -1):
    if disk_block_2[a][0] != '.':
        for b in range(a):
            if disk_block_2[b][0] == '.' and disk_block_2[b][1] >= len(disk_block_2[a]):
                disk_block_2[b][1] -= len(disk_block_2[a])
                disk_block_2.insert(b, disk_block_2[a].copy())
                disk_block_2[a+1] = ['.', len(disk_block_2[a+1])]
                break

index = 0
for a in disk_block_2:
    if a[0] == '.':
        index += a[1]
    else:
        for b in a:
            ans2 += int(b) * index
            index += 1

print("PART 1", ans1)
print("PART 2", ans2)

