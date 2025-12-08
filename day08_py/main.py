from pathlib import Path

import numpy as np


def part1(file: Path, num_connections: int) -> None:
    input = []
    with open(file) as f:
        for line in f:
            input.append(line.strip())
    length = len(input)

    # collect all xyz positions in array
    positions = np.zeros((length, 3))
    for ind in range(length):
        (x, y, z) = input[ind].split(",")
        positions[ind][0] = int(x)
        positions[ind][1] = int(y)
        positions[ind][2] = int(z)
    # print(f"{positions=}")

    # calculate all distances
    distances = []
    for ind1 in range(length):
        for ind2 in range(ind1 + 1, length):
            dx_square = (positions[ind1][0] - positions[ind2][0]) ** 2
            dy_square = (positions[ind1][1] - positions[ind2][1]) ** 2
            dz_square = (positions[ind1][2] - positions[ind2][2]) ** 2
            dist = np.sqrt(dx_square + dy_square + dz_square)
            distances.append((dist, ind1, ind2))
    # print(f"{distances=}")
    distances_sorted = sorted(distances, key=lambda x: x[0])
    # print(distances_sorted[0:10])

    # find circuits
    _, ind1, ind2 = distances_sorted[0]
    circuits = [[ind1, ind2]]
    for ind_connection in range(1, num_connections):
        _, ind1, ind2 = distances_sorted[ind_connection]
        # check where to append indices
        added_to_existing = False
        for circuit in circuits:
            if ind1 in circuit:
                circuit.append(ind2)
                added_to_existing = True
                break
            elif ind2 in circuit:
                circuit.append(ind1)
                added_to_existing = True
                break
        # create new circuit if required
        if not added_to_existing:
            circuits.append([ind1, ind2])
        # regular cleanup to remove duplicates
        for ind, circuit in enumerate(circuits):
            circuits[ind] = list(set(circuit))
        # combine circuits which now belong together
        all_in_order = False
        while not all_in_order:
            restart = False
            for ind1, circuit1 in enumerate(circuits):
                for ind2 in range(ind1 + 1, len(circuits)):
                    circuit2 = circuits[ind2]
                    common = set(circuit1) & set(circuit2)
                    if bool(common):
                        # print(common)
                        circuits.pop(ind2)
                        circuits.pop(ind1)
                        circuits.append(list(set(circuit1 + circuit2)))
                        restart = True
                        break
                if restart:
                    # start while loop anew until done
                    break
            all_in_order = True
    # print(f"{circuits=}")

    # get answer for part 1
    circuits.sort(key=len, reverse=True)
    answer = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
    print(f"Answer for part 1: {answer}")


if __name__ == "__main__":
    test = False
    if test:
        file = Path("day08_py/test.txt")
        part1(file, 10)
    else:
        file = Path("day08_py/input.txt")
        part1(file, 1000)
