import numpy as np

directions = {
    '^': (-1, 0, 'X', '>'),
    '>': (0, 1, 'X', 'v'),
    '<': (0, -1, 'X', '^'),
    'v': (1, 0, 'X', '<')
}

def print_map(m):
    for a in m:
        print(' '.join(a))
    print()

def search_map(test_map, extra_obs = False):
    guard = [[index, row.index('^')] for index, row in enumerate(test_map) if '^' in row][0]

    test_map = np.array(test_map)

    turn = False
    while True:
        guard_dir = test_map[guard[0]][guard[1]]

        x, y, marker, next_dir = directions[guard_dir]

        next_guard = [guard[0] + x, guard[1] + y]
        next_next_guard = [next_guard[0] + x, next_guard[1] + y]

        if 0 > next_guard[0] or next_guard[0] >= len(test_map) or 0 > next_guard[1] or next_guard[1] >= len(test_map[0]):
            test_map[guard[0]][guard[1]] = marker
            return 0 if extra_obs else test_map
        elif test_map[next_guard[0]][next_guard[1]] in ['#', '0']:
            test_map[guard[0]][guard[1]] = next_dir
            turn = True
        elif (extra_obs and
              (not (0 > next_next_guard[0] or next_next_guard[0] >= len(test_map) or 0 > next_next_guard[1] or next_next_guard[1] >= len(test_map[0]))
              and test_map[next_guard[0]][next_guard[1]] == '+'
              and test_map[next_next_guard[0]][next_next_guard[1]] in ['#', '0'])):
            return 1
        else:
            test_map[guard[0]][guard[1]] = marker if not turn else '+'
            guard = next_guard.copy()
            test_map[guard[0]][guard[1]] = guard_dir
            turn = False


mapped_area = [list(a.strip()) for a in open("input.txt", "r").readlines()]
mapped_area_2 = [list(a.strip()) for a in open("input.txt", "r").readlines()]

ans1 = 0
ans2 = 0

# PART 1
mapped_area = search_map(mapped_area)
ans1 = sum(a.count('X') + a.count('+') for a in mapped_area.tolist())

print(ans1)

# PART 2
c = 1
t = len(mapped_area_2) * len(mapped_area_2[0])
for a in range(len(mapped_area_2)):
    for b in range(len(mapped_area_2[0])):
        # print(f"position {c} of {t}")
        map_copy = mapped_area_2.copy()
        if map_copy[a][b] != '.':
            continue

        map_copy[a][b] = '0'

        ans2 +=  search_map(map_copy, extra_obs = True)

        mapped_area_2[a][b] = '.'
        c+=1

print(ans2)
