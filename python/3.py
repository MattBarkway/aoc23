import itertools
import re
from operator import add, mul

from loading import load_input


def run():
    schematic = load_input("3.txt")

    symbols = get_symbols(schematic)
    part_nums = get_part_nums(schematic, symbols)

    print(sum(part_nums))

    # pt2

    gears = get_gears(schematic)
    ratios = get_gear_ratios(schematic, gears)

    print(sum(ratios))


def get_symbols(schematic: list[str]) -> list[tuple[int, int]]:
    return get_match_coords(schematic, r"([^0-9.\n])")


def get_match_coords(schematic: list[str], pattern: str) -> list[tuple[int, int]]:
    coords = []
    for idx, line in enumerate(schematic):
        row = idx
        for match in re.finditer(pattern, line):
            coords.append((match.start(), row))
    return coords


def get_gears(schematic: list[str]) -> list[tuple[int, int]]:
    return get_match_coords(schematic, r"(\*)")


def get_part_nums(schematic: list[str], symbols: list[tuple[int, int]]) -> list[int]:
    part_nums = []
    for symbol in symbols:
        if parts_nums := get_parts_nums(symbol, schematic):
            part_nums.extend(parts_nums)
    return part_nums


def get_parts_nums(symbol: tuple[int, int], schematic: list[str]) -> list[int]:
    surrounding_nums = []
    for move in itertools.product(*[(-1, 0, 1)] * 2):
        if move == (0, 0):
            continue
        neighbour = tuple(map(add, symbol, move))
        token = schematic[neighbour[1]][neighbour[0]]
        if token in (".", "\n"):
            continue
        surrounding_nums.append(get_number(neighbour, schematic))  # noqa
    return list(set(surrounding_nums))


def get_number(location: tuple[int, int], schematic: list[str]) -> int:
    row = schematic[location[1]]
    for match in re.finditer(r"(\d+)", row):
        if match.start() <= location[0] <= match.end():
            return int(match.group())


def get_gear_ratios(schematic: list[str], symbols: list[tuple[int, int]]) -> list[int]:
    gear_ratios = []
    for symbol in symbols:
        if gear_ratio := get_gear_ratio(symbol, schematic):
            gear_ratios.append(gear_ratio)
    return gear_ratios


def get_gear_ratio(symbol: tuple[int, int], schematic: list[str]) -> int:
    surrounding_nums = get_parts_nums(symbol, schematic)
    if len(surrounding_nums) == 2:
        return mul(*surrounding_nums)


if __name__ == "__main__":
    run()
