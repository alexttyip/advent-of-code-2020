import sys

import numpy as np

np.set_printoptions(threshold=sys.maxsize)

offsets = np.array(np.meshgrid([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1])).T.reshape(-1, 4)


def main():
    space = read()
    for i in range(6):
        space = cycle(space)
        print(f"Cycle {i} done")

    print(space.sum())


def read():
    file = open("input.txt", "r")
    lines = file.read().splitlines()
    file.close()

    size = len(lines) + 2

    space = np.zeros([size] * 4, dtype=np.int64)

    height_offset = 1
    width_offset = 1
    z = size // 2
    w = size // 2

    i = 0
    while i < len(lines):
        j = 0
        line = lines[i]
        while j < len(line):
            char = lines[i][j]

            if char == '#':
                space[w, z, i + height_offset, j + width_offset] = 1
            j += 1
        i += 1

    return space


def cycle(space):
    size = space.shape[0]
    new_space = np.zeros([size + 2] * 4, dtype=np.int64)

    for iw in range(size):
        for iz in range(size):
            for iy in range(size):
                for ix in range(size):
                    is_active = check_neighbors(space, size, iw, iz, iy, ix)
                    new_space[iw + 1, iz + 1, iy + 1, ix + 1] = 1 if is_active else 0
    return new_space


def check_neighbors(space, size, *indexes):
    count = 0
    for offset in offsets:
        index = indexes + offset
        if np.array_equal(offset, [0] * 4):
            continue

        if np.min(index) < 0 or np.max(index) >= size:
            continue

        if space[tuple(index)] == 1:
            count += 1

        if count > 3:
            break

    return (space[tuple(indexes)] == 1 and 2 <= count <= 3) or (space[tuple(indexes)] == 0 and count == 3)


if __name__ == '__main__':
    main()
