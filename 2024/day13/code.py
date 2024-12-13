file = open("input.txt", "r").readlines()

ans1 = 0
ans2 = 0

for f in range(0, len(file), 4):
    a_x = int(file[f].strip().split(" ")[-2][2:-1])
    a_y = int(file[f].strip().split(" ")[-1][2:])
    b_x = int(file[f + 1].strip().split(" ")[-2][2:-1])
    b_y = int(file[f + 1].strip().split(" ")[-1][2:])
    p_x = int(file[f + 2].strip().split(" ")[-2][2:-1])
    p_y = int(file[f + 2].strip().split(" ")[-1][2:])
    p_x_2 = 10000000000000 + int(file[f + 2].strip().split(" ")[-2][2:-1])
    p_y_2 = 10000000000000 + int(file[f + 2].strip().split(" ")[-1][2:])

    a = (p_x * b_y - p_y * b_x) // (a_x * b_y - a_y * b_x)
    b = (p_x * a_y - p_y * a_x) // (a_y * b_x - a_x * b_y)
    if a_x * a + b_x * b == p_x and a_y * a + b_y * b == p_y:
        ans1 += (3*a)+b

    a = (p_x_2 * b_y - p_y_2 * b_x) // (a_x * b_y - a_y * b_x)
    b = (p_x_2 * a_y - p_y_2 * a_x) // (a_y * b_x - a_x * b_y)
    if a_x * a + b_x * b == p_x_2 and a_y * a + b_y * b == p_y_2:
        ans2 += (3*a)+b

    # PART 1
    # for a in range(100):
    #     for b in range(100):
    #         if a * a_x + b * b_x == p_x and a * a_y + b * b_y == p_y:
    #             results.append((3*a)+b)
    # if results:
    #     ans1 += min(results)

print("PART 1", ans1)
print("PART 2", ans2)

