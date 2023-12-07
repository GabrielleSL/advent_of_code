def main():
    f = open("input.txt", "r").readlines()

    priority_p1 = 0
    priority_p2 = 0

    for l in f:
        ruck, sack = l.strip()[:len(l) // 2], l.strip()[len(l) // 2:]
        intersection = (set(ruck) & set(sack)).pop()

        if intersection and intersection.islower():
            priority_p1 += (ord(intersection) - 96)
        elif intersection and intersection.isupper():
            priority_p1 += (ord(intersection) - 65 + 27)

    for l in range(0, len(f), 3):
        f[l] = f[l].strip()
        f[l + 1] = f[l + 1].strip()
        f[l + 2] = f[l + 2].strip()
        intersection = ((set(f[l]) & set(f[l + 1])) & set(f[l + 2])).pop()

        if intersection and intersection.islower():
            priority_p2 += (ord(intersection) - 96)
        elif intersection and intersection.isupper():
            priority_p2 += (ord(intersection) - 65 + 27)

    print(f"PART 1 ANSWER: {priority_p1}")
    print(f"PART 2 ANSWER: {priority_p2}")


main()
