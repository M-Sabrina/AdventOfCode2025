from pathlib import Path

import numpy as np


def part1(file: Path) -> None:
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    rows = len(input) - 1  # last line contains + or *
    val = input[0]
    val = val.split(" ")
    val = list(filter(None, val))
    cols = len(val)
    numbers = np.zeros((rows, cols))
    for row in range(rows):
        vals = input[row]
        vals = vals.split(" ")
        vals = list(filter(None, vals))
        for col in range(cols):
            numbers[row][col] = int(vals[col])
    # print(f"{numbers}")
    symbols = input[rows].split(" ")
    symbols = list(filter(None, symbols))
    # print(f"{symbols}")
    grand_total = 0
    for col in range(cols):
        # print(col)
        numbers_in_col = numbers[:, col]
        # print(numbers_in_col)
        # print(symbols[col])
        if symbols[col] == "+":
            # print(np.sum(numbers_in_col))
            grand_total += np.sum(numbers_in_col)
        else:
            multiply_res = 1
            for num in numbers_in_col:
                multiply_res *= num
            grand_total += multiply_res
    print(f"Answer for part 1: {int(grand_total)}")


if __name__ == "__main__":
    file = Path("day06_py/input.txt")
    # file = Path("day06_py/test.txt")
    part1(file)
    # part2(file)
