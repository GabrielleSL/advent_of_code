from functools import cache

stones =  list(map(int, open("input.txt", "r").readline().strip().split(" ")))

ans1 = 0
ans2 = 0

print(stones)

@cache # no caching = run time of forever
def update_stones(stone, c):
    if c == 0: return 1

    if stone == 0:
        return update_stones(1, c - 1)
    elif len(str(stone)) % 2 == 0:  # even number of digits
        return (update_stones(int(str(stone)[:int(len(str(stone)) / 2)]), c - 1) +
                update_stones(int(str(stone)[int(len(str(stone)) / 2):]), c - 1))
    else:
        return update_stones(stone * 2024, c - 1)

for a in stones:
    ans1 += update_stones(a, 25)
    ans2 += update_stones(a, 75)


print("PART 1", ans1)
print("PART 2", ans2)

