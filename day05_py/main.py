from __future__ import annotations

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


def part2_fail(file):
    fresh = 0
    ranges = []
    with open(file) as f:
        for line in f:
            if "-" in line:
                ranges.append(line.strip())
            elif line == "\n":
                break
    # print(ranges)
    fresh = set()
    for fresh_range in ranges:
        r = fresh_range.split("-")
        rmin = int(r[0])
        rmax = int(r[1])
        fresh.update(range(rmin, rmax + 1))
    print(f"Answer for part 2: {len(fresh)}")


class Range:
    lower: int
    upper: int

    def __init__(self, lower: int, upper: int) -> None:
        self.lower = lower
        self.upper = upper

    @staticmethod
    def from_str(input: str) -> Range:
        r = input.split("-")
        return Range(int(r[0]), int(r[1]))

    def __repr__(self) -> str:
        return f"{self.lower}-{self.upper}"

    def overlaps(self, other: Range) -> bool:
        """Checks if ranges overlap.

        Assumes sorted list --> self.lower is assumed lower than other.lower"""

        if self.upper >= other.lower:
            return True
        else:
            return False

    def combine(self, other: Range) -> Range:
        """Combines range with other range.

        Assumes sorted list --> self.lower is assumed lower than other.lower"""

        lower = self.lower
        upper = max(self.upper, other.upper)
        return Range(lower, upper)

    def count(self) -> int:
        return self.upper - self.lower + 1


def part2(file: Path) -> None:
    ranges: list[Range] = []
    with open(file) as f:
        for line in f:
            if "-" in line:
                r = Range.from_str(line.strip())
                ranges.append(r)
            elif line == "\n":
                break
    ranges.sort(key=lambda r: r.lower)
    # print(ranges)
    combined_ranges: list[Range] = []
    r_self = ranges[0]
    for r_other in ranges[1:]:
        if r_self.overlaps(r_other):
            r_self = r_self.combine(r_other)
        else:
            combined_ranges.append(r_self)
            r_self = r_other
    combined_ranges.append(r_self)
    # print(combined_ranges)
    fresh = 0
    for r in combined_ranges:
        fresh += r.count()
    print(f"Answer for part 2: {fresh}")


if __name__ == "__main__":
    file = Path("day05_py/input.txt")
    # file = Path("day05_py/test.txt")
    part1(file)
    part2(file)
