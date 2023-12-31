import itertools
import regex as re

from loading import load_input

VALID_NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_calibration(text):
    out = re.findall(r"(\d)", text)
    return int(f"{out[0]}{out[-1]}")


def get_calibration_pt2(text):
    numbers_pattern = r"(\d)|" + "|".join([f"({num})" for num in VALID_NUMBERS])
    filtered = tuple(filter(None, itertools.chain(*re.findall(numbers_pattern, text, overlapped=True))))

    def to_num(num):
        return VALID_NUMBERS.get(num, num)

    return int(f"{to_num(filtered[0])}{to_num(filtered[-1])}")


def run():
    inputs = load_input("1.txt")

    calibrations = []
    for line in inputs:
        calibrations.append(get_calibration(line))

    print(sum(calibrations))

    calibrations2 = []
    for line in inputs:
        calibrations2.append(get_calibration_pt2(line))

    print(sum(calibrations2))


if __name__ == "__main__":
    run()
