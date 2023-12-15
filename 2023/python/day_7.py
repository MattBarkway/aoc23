import collections

from loading import load_input


SCORES = {
    (5, 1): 1,  # High card
    (4, 2): 2,  # 1 pair
    (3, 2): 3,  # 2 pair
    (3, 3): 4,  # 3 of a kind
    (2, 3): 5,  # Full house
    (2, 4): 6,  # 4 of a kind
    (1, 5): 7,  # 5 of a kind
}


def run():
    dataset = load_input("7.txt")
    print(pt_1(dataset))
    print(pt_2(dataset))


def pt_1(rows: list[str]) -> int:
    return sum(
        (
            (rank + 1) * int(bid)
            for rank, (_, bid) in enumerate(
                sorted([row.split() for row in rows], key=into_score)
            )
        )
    )


def pt_2(rows: list[str]) -> int:
    return sum(
        (
            (rank + 1) * int(bid)
            for rank, (_, bid) in enumerate(
                sorted([row.split() for row in rows], key=into_score_pt2)
            )
        )
    )


def into_score(hand) -> int:
    card_nums = tuple(cards_to_nums(hand[0]))
    counts = collections.Counter(card_nums)
    score = SCORES[(len(counts), max(counts.values()))]
    return int(f"{score}{''.join((str(card_num).zfill(2) for card_num in card_nums))}")


def cards_to_nums(cards: str):
    return map(
        lambda x: int({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}.get(x, x)), cards
    )


def cards_to_nums_pt2(cards: str):
    return map(
        lambda x: int({"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}.get(x, x)), cards
    )


def into_score_pt2(hand) -> int:
    card_nums = tuple(cards_to_nums_pt2(hand[0]))
    counts = collections.Counter(card_nums)
    num_jokers = counts.pop(1, 0)
    score = SCORES[
        (
            1 if num_jokers == 5 else len(counts),
            max(counts.values()) + num_jokers if counts else num_jokers,
        )
    ]
    return int(f"{score}{''.join((str(card_num).zfill(2) for card_num in card_nums))}")


if __name__ == "__main__":
    run()
