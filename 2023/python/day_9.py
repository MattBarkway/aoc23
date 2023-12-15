import math

from loading import load_input
import numpy as np
from sklearn.metrics import mean_squared_error


def run():
    lines = load_input("9.txt")
    print(pt_1(lines))  # not 1684547978 - too low  1685148165
    print(pt_2(lines))


def pt_1(lines: list[str]) -> int:
    return sum(map(run_pt1, map(lambda x: list(map(int, x.split())), lines)))


def pt_2(lines: list[str]) -> int:
    return sum(map(run_pt2, map(lambda x: list(map(int, x.split())), lines)))


def run_pt1(line: list[int]):
    return get_next(line[-1], get_diffs(line)[:-1])


def get_diffs(line: list[int]):
    history = []
    diffs = line
    while any(diffs):
        diffs = [n - m for m, n in zip(diffs, diffs[1:])]
        history.append(diffs)
    return history


def run_pt2(line: list[int]):
    return get_previous(line[0], get_diffs(line)[:-1])


def get_next(val: int, history: list[list[int]]):
    store = 0
    for i in history[::-1]:
        store += i[-1]
    return val + store


def get_previous(val: int, history: list[list[int]]):
    store = 0
    for i in history[::-1]:
        store = i[0] - store
    return val - store


if __name__ == "__main__":
    run()
