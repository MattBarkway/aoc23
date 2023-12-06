from functools import reduce
from operator import mul

from loading import load_input, load_raw
from pydantic import BaseModel


class Race(BaseModel):
    distance: int
    time: int


def run():
    dataset = load_raw("6.txt")
    print(pt_1(dataset))
    print(pt_2(dataset))


def pt_1(dataset: str) -> int:
    races = load_races(dataset)
    winning_combos = [len(evaluate_race(race)) for race in races]
    out = reduce(mul, winning_combos)
    return out


def pt_2(dataset: str) -> int:
    race = load_race(dataset)
    winning_combos = evaluate_race(race)
    return len(winning_combos)


def load_races(dataset: str) -> list[Race]:
    return [
        Race(time=time, distance=distance)
        for time, distance in zip(
            *[map(int, x.split()[1:]) for x in dataset.split("\n")]
        )
    ]


def load_race(dataset: str) -> Race:
    return Race(
        **dict(
            zip(
                ["time", "distance"],
                [
                    int(x.split(maxsplit=1)[1].replace(" ", ""))
                    for x in dataset.split("\n")
                ],
            )
        )
    )


def evaluate_race(race: Race) -> list[int]:
    times = []
    for hold_time in range(1, race.time):
        distance = (race.time - hold_time) * hold_time
        if distance > race.distance:
            times.append(hold_time)
    return times


if __name__ == "__main__":
    run()
