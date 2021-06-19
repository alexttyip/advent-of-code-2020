import itertools

on = set()

file = open("input.txt", "r")
lines = file.read().splitlines()
file.close()

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '#':
            on.add((i, j, 0))

for _ in range(6):
    new_on = set()
    to_check = set()

    for (x, y, z) in on:
        for (dx, dy, dz) in itertools.product([-1, 0, 1], repeat=3):
            to_check.add((x + dx, y + dy, z + dz))

    for (x, y, z) in to_check:
        count = 0

        for (dx, dy, dz) in itertools.product([-1, 0, 1], repeat=3):
            if dx == dy == dz == 0:
                continue

            if (x + dx, y + dy, z + dz) in on:
                count += 1

        if ((x, y, z) in on and 2 <= count <= 3) or ((x, y, z) not in on and count == 3):
            new_on.add((x, y, z))
    on = new_on

print(len(on))
