def part1():
    f = open("input.txt", "r")

    count = 0

    for line in f:
        lower = int(line[0: line.index("-")])
        upper = int(line[line.index("-") + 1: line.index(" ")])

        char = line[line.index(":") - 1]

        string = line[7:]

        char_count = 0

        for c in string:
            if c == char:
                char_count = char_count + 1

        if lower <= char_count <= upper:
            count = count + 1

    return count


def part2():
    f = open("input.txt", "r")

    count = 0

    for line in f:
        index0 = int(line[0: line.index("-")]) - 1
        index1 = int(line[line.index("-") + 1: line.index(" ")]) - 1

        char = line[line.index(":") - 1]

        string = line[line.index(":") + 2:]

        if (string[index0] == char and string[index1] != char) or (string[index0] != char and string[index1] == char):
            # if count == 0:
                # print("index0: ", index0)
                # print("index1: ", index1)
                # print("char: ", char)
                # print("string: ", string)

            print(string[index0], ",", string[index1])
                # print(string[index1])
            count = count + 1
        # v
        # for c in string:
        #     if c == char:
        #         char_count = char_count + 1
        #
        # if lower <= char_count <= upper:
        #     count = count + 1

    return count


print(part2())
