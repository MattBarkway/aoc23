import day6

dataset = """Time:      7  15   30
Distance:  9  40  200"""


def test_pt_1():
    assert day6.pt_1(dataset) == 288


def test_pt_2():
    assert day6.pt_2(dataset) == 71503
