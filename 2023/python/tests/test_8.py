import pytest

import day_8

dataset_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

dataset_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


@pytest.mark.parametrize("dataset, expected", [(dataset_1, 2), (dataset_2, 6)])
def test_pt_1(dataset, expected):
    assert day8.pt_1(dataset) == expected


def test_pt_2():
    assert day8.pt_2(dataset_1) == 5905
