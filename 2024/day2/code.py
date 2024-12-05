def is_safe(level):
    if not(sorted(level) == level or sorted(level, reverse=True) == level):
        return 0

    diffs = [abs(a - b) for a, b in zip(level, level[1:])]

    if all([1 <= a <= 3 for a in diffs]):
        return 1

    return 0


file = open("input.txt", "r").readlines()

ans1 = 0
ans2 = 0

for l in file:
    report = list(map(int, l.strip().split()))

    safe = is_safe(report)
    ans1 += safe
    ans2 += safe

    if not safe:
        for a in range(len(report)):
            safe = is_safe([b for c, b in enumerate(report) if c != a])
            if safe:
                ans2 += safe
                break

print("PART 1:", ans1)

print("PART 2:", ans2)
