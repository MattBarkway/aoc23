import itertools

from loading import load_raw


def run():
    dataset = load_raw("8.txt")
    print(pt_1(dataset))
    print(pt_2(dataset))


def pt_1(data: str) -> ...:
    sides, _, *nodes = data.split("\n")
    sides = map(lambda s: {"L": 0}.get(s, 1), sides)
    nodes = map(
            lambda v: (v[0], v[1][1:-1].split(", ")),
            map(lambda x: x.split(" = "), nodes),
        )

    target = "ZZZ"
    node_dict = dict(nodes)
    first, current = list(node_dict.keys())[0], None
    for idx, side in enumerate(itertools.cycle(sides)):
        if not current:
            current = first
        if current == target:
            return idx
        current = node_dict[current][side]


def pt_2(data: str) -> ...:
    ...


if __name__ == "__main__":
    run()
