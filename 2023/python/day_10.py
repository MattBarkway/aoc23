import collections
from operator import add

from pydantic import BaseModel

from loading import load_raw


def run():
    dataset = load_raw("10.txt")
    print(pt_1(dataset))
    print(pt_2(dataset))


def get_start(lines: list[str]):
    for idx1, line in enumerate(lines):
        if "S" not in line:
            continue
        for idx2, char in enumerate(line):
            if char == "S":
                return idx2, idx1


CONNECTORS = {
    (0, 1): ["|", "7", "F"],
    (1, 0): ["-", "7", "J"],
    (0, -1): ["|", "J", "L"],
    (-1, 0): ["-", "F", "L"],
}
ALL_MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]
PIPES = {
    "L": [(1, 0), (0, 1)],
    "J": [(-1, 0), (0, 1)],
    "7": [(0, -1), (-1, 0)],
    "F": [(0, -1), (1, 0)],
    "|": [(0, 1), (0, -1)],
    "-": [(-1, 0), (1, 0)],
    "S": ALL_MOVES,
}


class Map(BaseModel):
    grid: list[str]
    nodes: list["Node"] = []

    def get_connections(self, node) -> list["Node"]:
        connections = []
        for move, neighbour in node.possible_neighbours.items():
            expected = CONNECTORS[move]
            token = self.grid[neighbour[1]][neighbour[0]]
            if token in expected and neighbour not in self.nodes:
                connections.append(
                    Node(coords=neighbour, pipe=token, distance=node.distance + 1)
                )
        return connections

    def draw_loop(self):
        start = get_start(self.grid)
        pos = start
        start = Node(
            coords=pos,
            pipe=self.grid[pos[1]][pos[0]],
            connections=[],
            distance=0,
        )
        done = []
        to_check = collections.deque([start])
        while to_check:
            node = to_check.pop()
            node.connections = [i for i in self.get_connections(node) if i not in done]
            to_check.extendleft(node.connections)
            done.append(node)
        return done


class Node(BaseModel):
    coords: tuple[int, int]
    pipe: str
    connections: list["Node"] = []
    distance: int

    @property
    def possible_neighbours(self):
        return {move: tuple(map(add, self.coords, move)) for move in PIPES[self.pipe]}

    def __eq__(self, other):
        return self.coords == other.coords

    def __repr__(self):
        return f"Node(distance={self.distance})"


def pt_1(data: str) -> int:
    m = Map(grid=data.split("\n")[::-1])
    loop = m.draw_loop()
    return max(node.distance for node in loop)


def pt_2(data: str) -> ...:
    ...


if __name__ == "__main__":
    run()
