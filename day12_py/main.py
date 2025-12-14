from pathlib import Path


def part1(file: Path) -> None:
    answer = 0
    with open(file) as f:
        for line in f:
            line = line.strip()

    print(f"Answer for part 1: {answer}")


if __name__ == "__main__":
    # file = Path("day12_py/input.txt")
    file = Path("day12_py/test.txt")
    part1(file)
    # part2(file)
