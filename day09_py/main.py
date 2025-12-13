import bisect
from collections import defaultdict
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


def part2(file):
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    length = len(input)

    red_tiles = np.zeros((length, 2), dtype=int)
    for ind in range(length):
        (x, y) = input[ind].split(",")
        x = int(x)
        y = int(y)
        red_tiles[ind][0] = x
        red_tiles[ind][1] = y
    edges = []
    for ind in range(length):
        x1 = red_tiles[ind][0]
        y1 = red_tiles[ind][1]
        if ind == length - 1:
            x2 = red_tiles[0][0]
            y2 = red_tiles[0][1]
        else:
            x2 = red_tiles[ind + 1][0]
            y2 = red_tiles[ind + 1][1]
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                edges.append((x, y1))
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                edges.append((x1, y))
    edges = set(edges)

    x_to_ys = defaultdict(list)
    y_to_xs = defaultdict(list)
    for x, y in edges:
        x_to_ys[x].append(y)
        y_to_xs[y].append(x)
    for x in x_to_ys:
        x_to_ys[x].sort()
    for y in y_to_xs:
        y_to_xs[y].sort()
    areas = []
    for ind1 in range(length):
        for ind2 in range(ind1 + 1, length):
            areas.append(
                (
                    int(
                        np.abs(red_tiles[ind1, 0] - red_tiles[ind2, 0] + 1)
                        * np.abs(red_tiles[ind1, 1] - red_tiles[ind2, 1] + 1)
                    ),
                    ind1,
                    ind2,
                )
            )
    areas.sort(reverse=True)
    for area, ind1, ind2 in areas:
        x1 = red_tiles[ind1][0]
        y1 = red_tiles[ind1][1]
        x2 = red_tiles[ind2][0]
        y2 = red_tiles[ind2][1]
        edges_rectangle = []
        for x in range(min(x1, x2), max(x1, x2) + 1):
            edges_rectangle.append((x, y1))
            edges_rectangle.append((x, y2))
        for y in range(min(y1, y2) + 1, max(y1, y2)):
            edges_rectangle.append((x1, y))
            edges_rectangle.append((x2, y))
        valid = True
        for x, y in edges_rectangle:
            if (x, y) in edges:
                continue
            y_candidates = x_to_ys[x]
            idx = bisect.bisect_left(y_candidates, y)
            has_below = idx > 0
            has_above = idx < len(y_candidates) - 0
            x_candidates = y_to_xs[y]
            idx2 = bisect.bisect_left(x_candidates, x)
            has_left = idx2 > 0
            has_right = idx2 < len(x_candidates) - 0
            if not (has_below and has_above and has_left and has_right):
                valid = False
                break
        if valid:
            print(f"Answer for part 2: {area}")
            return


if __name__ == "__main__":
    file = Path("day09_py/input.txt")
    # file = Path("day09_py/test.txt")
    part1(file)
    part2(file)
