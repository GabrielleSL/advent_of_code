instructions = [a.strip().split("|") for a in open("input.txt", "r").readlines()]
manuals = [a.strip().split(",") for a in open("input2.txt", "r").readlines()]

ans1 = 0
ans2 = 0

correct_manuals = []
incorrect_manuals = []

for a in manuals:
    correct = True
    for b in instructions:
        if b[0] in a and b[1] in a:
            if a.index(b[0]) < a.index(b[1]):
                continue
            else:
                correct = False
                break

    if correct:
        correct_manuals.append(a.copy())
    else:
        incorrect_manuals.append(a.copy())

ans1 = sum([int(a[int((len(a) - 1)/2)]) for a in correct_manuals])

for a in incorrect_manuals:
    while True:
        correct = True
        for b in instructions:
            if b[0] in a and b[1] in a:
                if a.index(b[0]) < a.index(b[1]):
                    continue
                else:
                    a[a.index(b[0])], a[a.index(b[1])] = a[a.index(b[1])], a[a.index(b[0])]
                    correct = False

        if correct:
            break

ans2 = sum([int(a[int((len(a) - 1)/2)]) for a in incorrect_manuals])

print(ans1)
print(ans2)