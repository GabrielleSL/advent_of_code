def main():
    f = open("input.txt", "r").readlines()

    full_overlaps = 0
    partial_overlap = 0

    for i in f:
        elf1 = list(map(int, i.strip().split(",")[0].split("-")))
        elf2 = list(map(int, i.strip().split(",")[1].split("-")))

        if ((elf1[0] >= elf2[0] and elf1[1] <= elf2[1])
                or (elf2[0] >= elf1[0] and elf2[1] <= elf1[1])):
            full_overlaps += 1

        if ((elf1[0] <= elf2[0] <= elf1[1])
                or (elf1[0] <= elf2[1] <= elf1[1])
                or (elf2[0] <= elf1[0] <= elf2[1])
                or (elf2[0] <= elf1[1] <= elf2[1])):
            partial_overlap += 1

    print(f"PART 1 ANSWER: {full_overlaps}")
    print(f"PART 2 ANSWER: {partial_overlap}")


main()
