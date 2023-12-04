def part1():
    f = open("day1_input.txt", "r")

    total_points = 0

    for card in f:
        card_points = 0
        numbers = card.strip().split(": ")[1].split(" | ")
        win_num = numbers[0].lstrip().replace("  ", " ").split(" ")
        your_num = numbers[1].lstrip().replace("  ", " ").split(" ")

        print(numbers)
        print(win_num)
        print(your_num)

        for n in your_num:
            if n in win_num:
                if card_points == 0: card_points = 1
                else: card_points *= 2

        total_points += card_points

    print(total_points)


def part2():
    f = open("day1_input.txt", "r").readlines()
    total_cards = [1] * len(f)

    for card in f:
        card_points = 0
        card_num = int(card.strip().split(": ")[0].split(" ")[-1])
        numbers = card.strip().split(": ")[1].split(" | ")
        win_num = numbers[0].lstrip().replace("  ", " ").split(" ")
        your_num = numbers[1].lstrip().replace("  ", " ").split(" ")

        for n in your_num:
            if n in win_num:
                card_points += 1

        for i in range(0, card_points):
            if card_num + i > len(total_cards):
                break
            total_cards[card_num + i] += total_cards[card_num-1]

    print(sum(total_cards))


# part1()
part2()
