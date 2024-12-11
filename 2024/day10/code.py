def trail_iter(top_map, curr, pos_x, pos_y, res = set()):
    next_pos = set()
    if pos_x + 1 < len(top_map[0]) and top_map[pos_x + 1][pos_y].isdigit() and int(top_map[pos_x + 1][pos_y]) == (curr + 1):
        next_pos.add((pos_x + 1, pos_y))

    if pos_x - 1 >= 0 and top_map[pos_x - 1][pos_y].isdigit() and int(top_map[pos_x - 1][pos_y]) == (curr + 1):
        next_pos.add((pos_x - 1, pos_y))

    if pos_y + 1 < len(top_map) and top_map[pos_x][pos_y + 1].isdigit() and int(top_map[pos_x][pos_y + 1]) == (curr + 1):
        next_pos.add((pos_x, pos_y + 1))

    if pos_y - 1 >= 0 and top_map[pos_x][pos_y - 1].isdigit() and int(top_map[pos_x][pos_y - 1]) == (curr + 1):
        next_pos.add((pos_x, pos_y - 1))

    for a in next_pos:
        if curr + 1 == 9:
            res.add(a)
        else:
            res.union(trail_iter(top_map, curr + 1, a[0], a[1], res))
    return res

def trail_iter_2(top_map, curr, pos_x, pos_y, res = []):
    next_pos = []
    if pos_x + 1 < len(top_map[0]) and top_map[pos_x + 1][pos_y].isdigit() and int(top_map[pos_x + 1][pos_y]) == (curr + 1):
        next_pos.append((pos_x + 1, pos_y))

    if pos_x - 1 >= 0 and top_map[pos_x - 1][pos_y].isdigit() and int(top_map[pos_x - 1][pos_y]) == (curr + 1):
        next_pos.append((pos_x - 1, pos_y))

    if pos_y + 1 < len(top_map) and top_map[pos_x][pos_y + 1].isdigit() and int(top_map[pos_x][pos_y + 1]) == (curr + 1):
        next_pos.append((pos_x, pos_y + 1))

    if pos_y - 1 >= 0 and top_map[pos_x][pos_y - 1].isdigit() and int(top_map[pos_x][pos_y - 1]) == (curr + 1):
        next_pos.append((pos_x, pos_y - 1))

    for a in next_pos:
        if curr + 1 == 9:
            res.append(a)
        else:
            trail_iter_2(top_map, curr + 1, a[0], a[1], res)
    return res

file = [list(a.strip()) for a in open("input.txt", "r").readlines()]

ans1 = 0
ans2 = 0

for a in range(len(file)):
    for b in range(len(file[0])):
        if file[a][b].isdigit() and int(file[a][b]) == 0:
            results = trail_iter(file, 0, a, b, set([]))
            ans1 += len(results)

            results_2 = trail_iter_2(file, 0, a, b, [])
            ans2 += len(results_2)


print("PART 1", ans1)
print("PART 2", ans2)

