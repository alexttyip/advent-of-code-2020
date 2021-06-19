import itertools

on = set()

file = open("input.txt", "r")
lines = file.read().splitlines()
file.close()

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '#':
            on.add((i, j, 0, 0))

for _ in range(6):
    new_on = set()
    to_check = set()

    for (x, y, z, w) in on:
        for (dx, dy, dz, dw) in itertools.product([-1, 0, 1], repeat=4):
            to_check.add((x + dx, y + dy, z + dz, w + dw))

    for (x, y, z, w) in to_check:
        count = 0

        for (dx, dy, dz, dw) in itertools.product([-1, 0, 1], repeat=4):
            if dx == dy == dz == dw == 0:
                continue

            if (x + dx, y + dy, z + dz, w + dw) in on:
                count += 1

        if ((x, y, z, w) in on and 2 <= count <= 3) or ((x, y, z, w) not in on and count == 3):
            new_on.add((x, y, z, w))
    on = new_on

print(len(on))
