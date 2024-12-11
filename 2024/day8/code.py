antinodes_file_2 = [list(a.strip()) for a in open("input.txt", "r").readlines()]

def all_antinodes(max_x, max_y, node1, node2, diff_x, diff_y):
    antinodes_nodes = set()

    if node1[1] > node2[1]:
        y, x = node1
        while True:
            y = y - diff_y
            x = x + diff_x

            if y >= max_y or y < 0 or x >= max_x or x < 0:
                break

            antinodes_file_2[y][x] = '#'
            antinodes_nodes.add((y, x))

        y, x = node2
        while True:
            y = y + diff_y
            x = x - diff_x

            if y >= max_y or y < 0 or x >= max_x or x < 0:
                break

            antinodes_file_2[y][x] = '#'
            antinodes_nodes.add((y, x))

    else:
        y, x = node1
        while True:
            y = y - diff_y
            x = x - diff_x

            if y >= max_y or y < 0 or x >= max_x or x < 0:
                break

            antinodes_file_2[y][x] = '#'
            antinodes_nodes.add((y, x))

        y, x = node2
        while True:
            y = y + diff_y
            x = x + diff_x

            if y >= max_y or y < 0 or x >= max_x or x < 0:
                break

            antinodes_file_2[y][x] = '#'
            antinodes_nodes.add((y, x))

    return antinodes_nodes

file = [list(a.strip()) for a in open("input.txt", "r").readlines()]
antinodes_file = [list(a.strip()) for a in open("input.txt", "r").readlines()]

ans1 = set()
ans2 = set()

nodes = {}

for a in range(len(file)):
    for b in range(len(file[0])):
        if file[a][b] != '.':
            node = file[a][b]
            ans2.add((a,b))
            if node in nodes.keys():
                nodes[node].append((a, b))
            else:
                nodes[node] = [(a, b)]

for a, b in nodes.items():
    for c in range(len(b) - 1):
        for d in range(c+1, len(b)):
            y_diff = abs(b[d][0] - b[c][0])
            x_diff = abs(b[d][1] - b[c][1])
            if b[c][1] > b[d][1]:
                antinodes = [(b[c][0] - y_diff, b[c][1] + x_diff), (b[d][0] + y_diff, b[d][1] - x_diff)]
            else:
                antinodes = [(b[c][0] - y_diff, b[c][1] - x_diff), (b[d][0] + y_diff, b[d][1] + x_diff)]
            for e in antinodes:
                if not (e[0] >= len(file) or e[0] < 0 or e[1] >= len(file[0]) or e[1] < 0):
                    antinodes_file[e[0]][e[1]] = '#'
                    ans1.add(e)

            ans2 = ans2.union(all_antinodes(len(file[0]), len(file), b[c], b[d], x_diff, y_diff))

# for a in antinodes_file:
#     print(' '.join(b for b in a))

# for a in antinodes_file_2:
#     print(' '.join(b for b in a))

print("PART 1", len(ans1))
print("PART 2", len(ans2))

