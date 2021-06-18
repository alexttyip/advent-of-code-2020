import sys

import numpy as np

np.set_printoptions(threshold=sys.maxsize)

size = 20
offsets = np.array(np.meshgrid([-1, 0, 1], [-1, 0, 1], [-1, 0, 1])).T.reshape(-1, 3)


def main():
    space = read()
    for i in range(6):
        space = cycle(space)
        print(f"Cycle {i} done")

    print(space.sum())


def read():
    space = np.zeros((size, size, size), dtype=np.int64)

    file = open("input.txt", "r")
    lines = file.read().splitlines()
    file.close()

    height_offset = size // 2 - len(lines) // 2
    width_offset = size // 2 - len(lines[0]) // 2
    z = size // 2

    i = 0
    while i < len(lines):
        j = 0
        line = lines[i]
        while j < len(line):
            char = lines[i][j]

            if char == '#':
                space[z, i + height_offset, j + width_offset] = 1
            j += 1
        i += 1

    return space


def cycle(space):
    new_space = np.zeros((size, size, size), dtype=np.int64)

    for iz in range(size):
        for iy in range(size):
            for ix in range(size):
                is_active = check_neighbors(space, iz, iy, ix)
                new_space[iz, iy, ix] = 1 if is_active else 0
    return new_space


def check_neighbors(space, *indexes):
    count = 0
    for offset in offsets:
        index = indexes + offset
        if np.array_equal(offset, [0, 0, 0]):
            continue

        if np.min(index) < 0 or np.max(index) >= size:
            if space[tuple(indexes)] == 1:
                print("OUT OF BOUNDS")
                sys.exit()
            else:
                continue

        if space[tuple(index)] == 1:
            count += 1

        if count > 3:
            break

    return (space[tuple(indexes)] == 1 and 2 <= count <= 3) or (space[tuple(indexes)] == 0 and count == 3)


if __name__ == '__main__':
    main()
