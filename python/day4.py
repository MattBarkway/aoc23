import collections

from loading import load_input


def run():
    cards = load_input("4.txt")
    print(pt_1(cards))
    print(pt_2(cards))


def pt_1(cards: list[str]) -> int:
    score = []
    for card in cards:
        my_winners = get_winners(card)
        if my_winners:
            score.append(2 ** (len(my_winners) - 1))

    return sum(score)


def pt_2(cards: list[str]) -> int:
    copies: dict[int, int] = collections.defaultdict(int)

    for card in cards:
        card_str, rest = card.split(": ")
        card_num = int(card_str.split()[1])
        num_copies = copies[card_num]
        my_winners = get_winners_pt2(rest)
        for i in range(len(my_winners)):
            copies[card_num + i + 1] += 1 + num_copies
    return sum([v + 1 for v in copies.values()])


def get_winners(card: str) -> list[int]:
    card_num, rest = card.split(": ")
    winning_str, mine_str = rest.split("|")
    winning = str_to_nums(winning_str)
    mine = str_to_nums(mine_str)
    return [i for i in mine if i in winning]


def get_winners_pt2(rest: str) -> list[int]:
    winning_str, mine_str = rest.split("|")
    winning = str_to_nums(winning_str)
    mine = str_to_nums(mine_str)
    return [i for i in mine if i in winning]


def str_to_nums(num_str: str) -> list[int]:
    return [int(i.strip()) for i in num_str.split()]


if __name__ == "__main__":
    run()
