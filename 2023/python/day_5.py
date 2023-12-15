import itertools
from functools import reduce

from loading import load_raw


def run():
    dataset = load_raw("5.txt")
    print(pt_1(dataset))
    print(pt_2(dataset))


def pt_1(dataset: str) -> int:
    seeds, *maps = dataset.split("\n\n")
    seeds = tuple(map(int, seeds.split()[1:]))
    maps = [[tuple(map(int, n.split())) for n in m.split("\n")[1:]] for m in maps]
    return min(reduce(evaluate, maps, seed) for seed in seeds)


def pt_2(dataset: str) -> int:
    seeds, *maps = dataset.split("\n\n")
    seeds = tuple(map(int, seeds.split()[1:]))
    seeds = itertools.chain(
        *(range(x, x + y + 1) for x, y in zip(seeds[::2], seeds[1::2]))
    )
    maps = [[tuple(map(int, n.split())) for n in m.split("\n")[1:]] for m in maps]
    return min(reduce(evaluate, maps, seed) for seed in seeds)


def evaluate(val: int, m: list[tuple[int, int, int]]) -> int:
    for dest, source, _range in m:
        if source <= val <= source + _range:
            return val - source + dest
    return val


if __name__ == "__main__":
    run()
