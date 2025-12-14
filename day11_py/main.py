from pathlib import Path
from typing import Generator


def find_all_paths(
    graph: dict[str, list[str]], current_node: str, path: list[str] | None = None
) -> Generator[list[str], None, None]:
    # Initialize path on first call
    if path is None:
        path = []

    # Add current node to the path
    path = path + [current_node]

    # BASE CASE: We reached the destination
    if current_node == "out":
        yield path
        return

    for output in graph[current_node]:
        yield from find_all_paths(graph, output, path)


def part1(test: bool = False) -> None:
    if test:
        file = Path("day11_py/test.txt")
    else:
        file = Path("day11_py/input.txt")
    graph = dict()
    with open(file) as f:
        for line in f:
            line = line.strip().split(": ")
            input = line[0]
            outputs = line[1].split(" ")
            graph[input] = outputs
    # print(f"{graph:}")

    path_generator = find_all_paths(graph, "you")
    answer = 0
    # Iterate through the generator
    for p in path_generator:
        answer += 1

    print(f"Answer for part 1: {answer}")


def part2(test: bool = False) -> None:
    if test:
        file = Path("day11_py/test2.txt")
    else:
        file = Path("day11_py/input.txt")
    graph = dict()
    with open(file) as f:
        for line in f:
            line = line.strip().split(": ")
            input = line[0]
            outputs = line[1].split(" ")
            graph[input] = outputs
    # print(f"{graph:}")

    path_generator = find_all_paths(graph, "svr")
    answer = 0
    # Iterate through the generator
    for p in path_generator:
        if "dac" in p and "fft" in p:
            answer += 1

    print(f"Answer for part 2: {answer}")


if __name__ == "__main__":
    test = False
    part1(test)
    part2(test)
