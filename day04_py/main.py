from pathlib import Path

import numpy as np


def check_surroundings(map: np.array, row: int, col: int, rows: int, cols: int):
    count = 0

    if row - 1 >= 0 and col - 1 >= 0 and map[row - 1][col - 1] == 1:
        count = count + 1
    if row - 1 >= 0 and map[row - 1][col] == 1:
        count = count + 1
    if row - 1 >= 0 and col + 1 < cols and map[row - 1][col + 1] == 1:
        count = count + 1
    if col - 1 >= 0 and map[row][col - 1] == 1:
        count = count + 1
    if col + 1 < cols and map[row][col + 1] == 1:
        count = count + 1
    if row + 1 < rows and col - 1 >= 0 and map[row + 1][col - 1] == 1:
        count = count + 1
    if row + 1 < rows and map[row + 1][col] == 1:
        count = count + 1
    if row + 1 < rows and col + 1 < cols and map[row + 1][col + 1] == 1:
        count = count + 1

    if count >= 4:
        return False
    else:
        return True


def part1(file):
    map_original = np.loadtxt(file, dtype=str)
    rows = map_original.size
    cols = len(map_original[0])
    map = np.zeros((rows, cols))
    for r, row in enumerate(map_original):
        for c, string in enumerate(row):
            if string == "@":
                map[r, c] = 1
    # print(map)

    count_accessible = 0
    for row in range(rows):
        for col in range(cols):
            pos = map[row][col]
            if pos == 1:
                accessible = check_surroundings(map, row, col, rows, cols)
                if accessible:
                    count_accessible = count_accessible + 1
    print(f"Answer for part 1: {count_accessible}")


def part2(file):
    map_original = np.loadtxt(file, dtype=str)
    rows = map_original.size
    cols = len(map_original[0])
    map = np.zeros((rows, cols))
    for r, row in enumerate(map_original):
        for c, string in enumerate(row):
            if string == "@":
                map[r, c] = 1
    # print(map)

    count_accessible = 0
    while True:
        accessible_pos = []
        has_accessible = False
        for row in range(rows):
            for col in range(cols):
                pos = map[row][col]
                if pos == 1:
                    accessible = check_surroundings(map, row, col, rows, cols)
                    if accessible:
                        count_accessible = count_accessible + 1
                        accessible_pos.append((row, col))
                        has_accessible = True
        for pos in accessible_pos:
            (row, col) = pos
            map[row][col] = 0
        if not has_accessible:
            break

    print(f"Answer for part 2: {count_accessible}")


if __name__ == "__main__":
    file = Path("day04_py/input.txt")
    # file = Path("day04_py/test.txt")
    part1(file)
    part2(file)
