def main():
    f = open("input.txt", "r").readlines()
    stacks_p1 = [["B", "Q", "C"], ["R", "Q", "W", "Z"], ["B", "M", "R", "L", "V"], ["C", "Z", "H", "V", "T", "W"],
                 ["D", "Z", "H", "B", "N", "V", "G"], ["H", 'N', "P", 'C', "J", 'F', "V", "Q"],
                 ["D", "G", "T", 'R', "W", "Z", "S"], ["C", "G", "M", "N", "B", "W", "Z", "P"],
                 ["N", "J", "B", "M", "W", "Q", "F", "P"]]
    stacks_p2 = [["B", "Q", "C"], ["R", "Q", "W", "Z"], ["B", "M", "R", "L", "V"], ["C", "Z", "H", "V", "T", "W"],
                 ["D", "Z", "H", "B", "N", "V", "G"], ["H", 'N', "P", 'C', "J", 'F', "V", "Q"],
                 ["D", "G", "T", 'R', "W", "Z", "S"], ["C", "G", "M", "N", "B", "W", "Z", "P"],
                 ["N", "J", "B", "M", "W", "Q", "F", "P"]]

    for line in f:
        move_list = [int(line.strip().split(" ")[i]) for i in (1, 3, 5)]
        move_list2 = move_list
        for _i in range(move_list[0]):
            box_to_move = stacks_p1[move_list[1] - 1].pop(-1)
            stacks_p1[move_list[2] - 1].append(box_to_move)
        for i in range(move_list2[0] - 1, -1, -1):
            box_to_move = stacks_p2[move_list2[1] - 1].pop(-1 - i)
            stacks_p2[move_list2[2] - 1].append(box_to_move)

    answer_p1 = "".join([stacks_p1[i][-1] for i in range(len(stacks_p1))])
    answer_p2 = "".join([stacks_p2[i][-1] for i in range(len(stacks_p2))])

    print(f"PART 1 ANSWER: {answer_p1}")
    print(f"PART 2 ANSWER: {answer_p2}")


main()
