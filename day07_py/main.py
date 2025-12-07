from pathlib import Path

import numpy as np


def part1(file):
    map_original = np.loadtxt(file, dtype=str)
    rows = map_original.size
    cols = len(map_original[0])
    map = np.zeros((rows, cols))
    for r, row in enumerate(map_original):
        for c, string in enumerate(row):
            if string == "^":
                map[r, c] = 2
            elif string == "S":
                map[r, c] = 1
    # print(map)
    beams_positions = map[0][:]
    splits = 0
    # print(beams_positions)
    for row in range(1, rows):
        splitter_positions = map[row][:]
        match = np.sum(splitter_positions * beams_positions)
        if match > 0:
            beams_positions_new = []
            beam_positions_remove = []
            for col in range(cols):
                if beams_positions[col] == 1 and splitter_positions[col] == 2:
                    beams_positions_new.append(col - 1)
                    beams_positions_new.append(col + 1)
                    beam_positions_remove.append(col)
                    splits += 1
            for col in beams_positions_new:
                if col >= 0 and col < cols:
                    beams_positions[col] = 1
            for col in beam_positions_remove:
                beams_positions[col] = 0
        # print(beams_positions)
    print(f"Answer for part 1: {splits}")


if __name__ == "__main__":
    file = Path("day07_py/input.txt")
    # file = Path("day07_py/test.txt")
    part1(file)
    # part2(file)
