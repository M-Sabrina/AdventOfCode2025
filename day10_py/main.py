from pathlib import Path


def part1(file: Path) -> None:
    input = []
    # Each line contains a single indicator light diagram in [square brackets],
    # one or more button wiring schematics in (parentheses),
    # and joltage requirements in {curly braces}.
    with open(file) as f:
        for line in f:
            input.append(line.strip())

    print(f"Answer for part 1: {0}")


if __name__ == "__main__":
    file = Path("day10_py/input.txt")
    # file = Path("day10_py/test.txt")
    part1(file)
    # part2(file)
