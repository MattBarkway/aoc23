import itertools
import re
from functools import reduce
from operator import sub, mul

from loading import load_input

TARGET_GAME = (12, 13, 14)
NULL = (0, 0, 0)
COLOURS = {
    "red": 0,
    "green": 1,
    "blue": 2,
}


def run():
    inputs = load_input("2.txt")
    nums = []
    for line in inputs:
        game_num = int(re.findall(r"Game (\d+):", line)[0])
        if is_valid_game(line):
            nums.append(game_num)
    print(sum(nums))

    # pt 2
    powers = []
    for line in inputs:
        samples = get_samples(line)
        max_tuple = [max(i) for i in zip(*samples)]
        powers.append(reduce(mul, max_tuple))
    print(sum(powers))


def is_valid_game(line):
    for sample in get_samples(line):
        if not len([i for i in map(sub, TARGET_GAME, sample) if i >= 0]) == 3:
            return False
    return True


def get_samples(line) -> list[tuple[int, int, int]]:
    sample_tuples = []
    for sample in re.sub(r"Game \d+: ", "", line).split(";"):
        sample_tuples.append(into_tuple(sample.split(", ")))
    return sample_tuples


def into_tuple(reads) -> tuple[int, int, int]:
    out = [0, 0, 0]
    for read in reads:
        num, colour = read.split()
        out[COLOURS.get(colour)] = int(num)
    return tuple(out)


if __name__ == '__main__':
    run()
