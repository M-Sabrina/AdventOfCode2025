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


def part2(file: Path) -> None:
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.replace("\n", ""))
    rows = len(input)
    cols = len(input[0])
    # print(input)

    grand_total = 0

    numbers = []
    numbers_ind = 0
    for col in range(cols):
        symbol_col = input[rows - 1][col]
        if not (symbol_col == " "):
            symbol = symbol_col
            # print(symbol)
            numbers = []
        val = ""
        for row in range(rows - 1):
            val += input[row][col]
        if val.replace(" ", "") == "":  # empty column
            numbers_ind = 0
            if symbol == "+":
                grand_total += sum(numbers)
            else:
                multiply_res = 1
                for num in numbers:
                    multiply_res *= num
                grand_total += multiply_res
            continue
        numbers.append(int(val))
        numbers_ind = numbers_ind + 1

    # final one:
    if symbol == "+":
        grand_total += sum(numbers)
    else:
        multiply_res = 1
        for num in numbers:
            multiply_res *= num
        grand_total += multiply_res

    print(f"Answer for part 2: {int(grand_total)}")


if __name__ == "__main__":
    file = Path("day06_py/input.txt")
    # file = Path("day06_py/test.txt")
    part1(file)
    part2(file)
