def main():
    f = open("input.txt", "r")

    points_p1 = 0
    round_points_p1 = {"X": 1, "Y": 2, "Z": 3,
                       "AX": 3, "BY": 3, "CZ": 3,
                       "AY": 6, "BZ": 6, "CX": 6,
                       "AZ": 0, "BX": 0, "CY": 0}

    points_p2 = 0
    round_points_p2 = {"X": 0, "Y": 3, "Z": 6,
                       "AX": 3, "AY": 1, "AZ": 2,
                       "BX": 1, "BY": 2, "BZ": 3,
                       "CX": 2, "CY": 3, "CZ": 1}

    for line in f:
        opponent, you = line.strip().split(" ")
        points_p1 += (round_points_p1.get(you) + round_points_p1.get(f"{opponent}{you}"))
        points_p2 += (round_points_p2.get(you) + round_points_p2.get(f"{opponent}{you}"))

    print(f"PART 1 ANSWER: {points_p1}")
    print(f"PART 2 ANSWER: {points_p2}")


main()
