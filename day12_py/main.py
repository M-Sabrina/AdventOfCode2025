from pathlib import Path


def part1(file: Path) -> None:
    """
    Solve the 2D packing puzzle using the Area Heuristic.

    For a general 2D packing problem, checking if total_item_area <= container_area
    is necessary but not sufficient (shapes might not fit due to geometry).

    However, for this specific puzzle input, the inputs are constructed such that
    any set of items satisfying the area constraint can actually be packed.
    This allows us to skip complex backtracking/tiling algorithms.
    """
    lines = file.read_text().split("\n")

    # Parse shape definitions: each shape has an area (count of '#' cells)
    shapes: dict[int, int] = {}
    # Parse regions: (width, height, list of counts per shape)
    regions: list[tuple[int, int, list[int]]] = []

    current_shape_id: int | None = None

    for line in lines:
        line = line.rstrip()

        # Check for shape header (e.g., "0:")
        if line.endswith(":") and line[:-1].isdigit():
            current_shape_id = int(line[:-1])
            shapes[current_shape_id] = 0
            continue

        # Check for region definition (e.g., "12x5: 1 0 1 0 2 2")
        if "x" in line and ": " in line:
            dimensions, counts_str = line.split(": ")
            w, h = map(int, dimensions.split("x"))
            counts = list(map(int, counts_str.split()))
            regions.append((w, h, counts))
            current_shape_id = None
            continue

        # If we're inside a shape definition, count '#' characters
        if current_shape_id is not None:
            shapes[current_shape_id] += line.count("#")

    # Count valid regions using the area heuristic:
    # A region can fit all presents if the total present area <= region area.
    # This is a heuristic that works for this puzzle's specific input construction.
    valid_count = 0
    for w, h, counts in regions:
        region_area = w * h
        needed_area = 0
        for shape_id, count in enumerate(counts):
            needed_area += count * shapes[shape_id]
        if needed_area <= region_area:
            valid_count += 1

    print(f"Answer for part 1: {valid_count}")


if __name__ == "__main__":
    file = Path("day12_py/input.txt")
    part1(file)
