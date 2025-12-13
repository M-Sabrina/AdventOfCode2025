from itertools import combinations_with_replacement
from pathlib import Path


def button_click(list1: list[int], list2: list[int]):
    for ind in range(len(list1)):
        list1[ind] = (list1[ind] + list2[ind]) % 2


def part1(file: Path) -> None:
    # Each line contains a single indicator light diagram in [square brackets],
    # one or more button wiring schematics in (parentheses),
    # and joltage requirements in {curly braces}.
    button_presses_total = 0
    with open(file) as f:
        for line in f:
            line = line.strip()
            indicator_diagram = line.split("]")[0][1:]
            buttons = line.split("{")[0].split("]")[1].strip().split(" ")
            indicators = [
                0 if c == "." else 1 for c in indicator_diagram
            ]  # ".##." -> 0110
            masks = []
            empty_mask = [0 for _ in indicators]
            for button in buttons:
                mask = empty_mask.copy()
                nums = button[1:-1].split(",")
                for num in nums:
                    mask[int(num)] = 1
                masks.append(mask)

            def solve():
                for i in range(1, 10):
                    for combination in combinations_with_replacement(masks, i):
                        lights = empty_mask.copy()
                        for mask in combination:
                            button_click(lights, mask)
                        if lights == indicators:
                            return i

            button_presses_total += solve()

    print(f"Answer for part 1: {button_presses_total}")


if __name__ == "__main__":
    file = Path("day10_py/input.txt")
    # file = Path("day10_py/test.txt")
    part1(file)
    # part2(file)
