from pathlib import Path

import numpy as np


def part1(file):
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    length = len(input)
    # collect all xy red_tiles in array
    red_tiles = np.zeros((length, 2))
    for ind in range(length):
        (x, y) = input[ind].split(",")
        red_tiles[ind][0] = int(x)
        red_tiles[ind][1] = int(y)
    # print(f"{red_tiles=}")
    areas = []
    for ind1 in range(length):
        for ind2 in range(ind1 + 1, length):
            areas.append(
                int(
                    np.abs(red_tiles[ind1, 0] - red_tiles[ind2, 0] + 1)
                    * np.abs(red_tiles[ind1, 1] - red_tiles[ind2, 1] + 1)
                )
            )
    print(f"Answer for part 1: {max(areas)}")


if __name__ == "__main__":
    file = Path("day09_py/input.txt")
    # file = Path("day09_py/test.txt")
    part1(file)
    # part2(file)
