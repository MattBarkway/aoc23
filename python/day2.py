import itertools
import re
from operator import sub

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
    # nums = []
    # for line in inputs:
    #     game_num = int(re.findall(r"Game (\d+):", line)[0])
    #     if is_valid_game(line):
    #         nums.append(game_num)
    # print(sum(nums))

    # pt 2
    powers = []
    for line in inputs:
        game_num = int(re.findall(r"Game (\d+):", line)[0])
        samples = get_samples(line)
        itertools.chain(*samples)
        max_tuple = [max(i) for i in zip(*samples)]
        powers.append(max_tuple[0] * max_tuple[1] * max_tuple[2])

    print(sum(powers))


def is_valid_game(line):
    samples = get_samples(line)
    for sample in samples:
        subtracted = [i for i in map(sub, TARGET_GAME, sample)]
        if not len([i for i in map(sub, TARGET_GAME, sample) if i >= 0]) == 3:
            return False
    return True


def get_samples(line) -> list[tuple[int, int, int]]:
    games = re.sub(r"Game \d+: ", "", line).split(";")
    sample_tuples = []
    for sample in games:
        reads = sample.split(", ")
        sample_tuple = into_tuple(reads)
        sample_tuples.append(sample_tuple)
    return sample_tuples


def into_tuple(reads) -> tuple[int, int, int]:
    out = [0, 0, 0]
    for read in reads:
        num, colour = read.split()
        idx = COLOURS.get(colour)
        out[idx] = int(num)
    return tuple(out)


if __name__ == '__main__':
    run()
