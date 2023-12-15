import pytest

import day7

dataset = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def test_pt_1():
    assert day7.pt_1(dataset.splitlines()) == 6440


def test_pt_2():
    assert day7.pt_2(dataset.splitlines()) == 5905


@pytest.mark.parametrize(
    "hand, expected",
    [("32T3K", 20302100313), ("T55J5", 41005051105), ("KK677", 31313060707)],
)
def test_into_score(hand, expected):
    assert day7.into_score((hand, None)) == expected


@pytest.mark.parametrize(
    "hand, expected",
    [("32T3K", 20302100313), ("T55J5", 61005050105), ("KK677", 31313060707)],
)
def test_into_score_pt2(hand, expected):
    assert day7.into_score_pt2((hand, None)) == expected
