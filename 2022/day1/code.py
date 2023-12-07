def main():
    f = open("input.txt", "r")

    cals = [0]

    for line in f:
        if line.strip() == "":
            cals.append(0)
        else:
            cals[-1] += int(line.strip())

    cals.sort()

    print(f"PART 1 ANSWER: {cals[-1]}")
    print(f"PART 2 ANSWER: {sum(cals[-3:])}")


main()
