import day_9

dataset = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def test_pt_1():
    assert day_9.pt_1(dataset.split("\n")) == 114


def test_pt_2():
    assert day_9.pt_2(dataset.split("\n")) == 2
