file = open("input.txt", "r").readlines()

left_list = []
right_list = []
ans1 = 0
ans2 = 0

for l in file:
    s_l = l.strip().split()
    left_list.append(s_l[0])
    right_list.append(s_l[1])

left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    ans1 += abs(int(left_list[i]) - int(right_list[i]))

print("PART 1:", ans1)

for num in left_list:
    r = right_list.count(num)
    ans2 += (int(num) * r)

print("PART 2:", ans2)

