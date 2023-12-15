import pytest

import day_10

dataset = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""

dataset2 = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""


def test_pt_1():
    assert day_10.pt_1(dataset) == 4


def test_pt_1_2():
    assert day_10.pt_1(dataset2) == 8


def test_pt_2():
    assert day_10.pt_2(dataset) == False
