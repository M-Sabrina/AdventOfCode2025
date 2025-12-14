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


def count_paths(
    graph: dict[str, list[str]],
    *,
    current_node: str,
    final_node: str,
    forbidden: frozenset[str],
    cache: dict[tuple[str, str, frozenset[str]], int],
) -> int:
    """Count all paths from node to end, avoiding forbidden nodes."""

    # graph doesn't need to be cached since it is immutable
    key = (current_node, final_node, forbidden)
    if key in cache:
        return cache[key]

    count = 0
    if current_node in forbidden:
        return 0
    elif current_node == final_node:
        return 1
    elif current_node == "out":
        return 0
    else:
        for output in graph[current_node]:
            count += count_paths(
                graph,
                current_node=output,
                final_node=final_node,
                forbidden=forbidden,
                cache=cache,
            )

    cache[key] = count
    return count


def part2(test: bool = False) -> None:
    if test:
        file = Path("day11_py/test2.txt")
    else:
        file = Path("day11_py/input.txt")

    graph: dict[str, list[str]] = {}
    cache: dict[tuple[str, str, frozenset[str]], int] = {}

    with open(file) as f:
        for line in f:
            line = line.strip().split(": ")
            input = line[0]
            outputs = line[1].split(" ")
            graph[input] = outputs
    # print(f"{graph:}")

    # Count paths for both orderings of dac and fft
    answer = 0

    # Ordering 1: svr -> dac -> fft -> out
    # We forbid fft in the first segment to avoid counting paths where fft comes before dac
    paths_svr_to_dac = count_paths(
        graph,
        current_node="svr",
        final_node="dac",
        forbidden=frozenset({"fft"}),
        cache=cache,
    )
    paths_dac_to_fft = count_paths(
        graph, current_node="dac", final_node="fft", forbidden=frozenset(), cache=cache
    )
    paths_fft_to_out = count_paths(
        graph, current_node="fft", final_node="out", forbidden=frozenset(), cache=cache
    )
    answer += paths_svr_to_dac * paths_dac_to_fft * paths_fft_to_out

    # Ordering 2: svr -> fft -> dac -> out
    # We forbid dac in the first segment to avoid counting paths where dac comes before fft
    paths_svr_to_fft = count_paths(
        graph,
        current_node="svr",
        final_node="fft",
        forbidden=frozenset({"dac"}),
        cache=cache,
    )
    paths_fft_to_dac = count_paths(
        graph, current_node="fft", final_node="dac", forbidden=frozenset(), cache=cache
    )
    paths_dac_to_out = count_paths(
        graph, current_node="dac", final_node="out", forbidden=frozenset(), cache=cache
    )
    answer += paths_svr_to_fft * paths_fft_to_dac * paths_dac_to_out

    print(f"Answer for part 2: {answer}")


if __name__ == "__main__":
    test = False
    part1(test)
    part2(test)
