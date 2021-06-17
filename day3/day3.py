def part1():
    return iterate(3, 1)
    # f = open("input.txt", "r")
    #
    # x = 0
    # count = 0
    #
    # for line in f:
    #     if line[x] == "#":
    #         count += 1
    #
    #     x = (x + 3) % len(line.strip())
    #
    # return count


def iterate(x_interval, y_interval):
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

    x = 0
    count = 0
    line_length = len(lines[0])

    for i in range(0, len(lines), y_interval):
        line = lines[i]
        if line[x] == "#":
            count += 1

        x = (x + x_interval) % line_length

    return count


def part2():
    return iterate(1, 1) * iterate(3, 1) * iterate(5, 1) * iterate(7, 1) * iterate(1, 2)


print(part2())
