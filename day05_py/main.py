from pathlib import Path


def part1(file):
    fresh = 0
    ranges = []
    available = []
    with open(file) as f:
        for line in f:
            if "-" in line:
                ranges.append(line.strip())
            elif line == "\n":
                continue
            else:
                available.append(int(line.strip()))
    # print(ranges)
    # print(available)
    for id in available:
        for fresh_range in ranges:
            r = fresh_range.split("-")
            rmin = int(r[0])
            rmax = int(r[1])
            if id >= rmin and id <= rmax:
                fresh = fresh + 1
                break
    print(f"Answer for part 1: {fresh}")


if __name__ == "__main__":
    file = Path("day05_py/input.txt")
    # file = Path("day05_py/test.txt")
    part1(file)
    # part2(file)
