def part1():
    with open("input.txt", "r") as f:
        ans = -1

        for line in f:
            row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
            col = int(line[7:].replace("L", "0").replace("R", "1"), 2)

            temp = row * 8 + col

            if temp > ans:
                ans = temp

        return ans


def part2():
    with open("input.txt", "r") as f:
        ids = []
        for line in f:
            row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
            col = int(line[7:].replace("L", "0").replace("R", "1"), 2)

            ids.append(row * 8 + col)

        ids.sort()

        for i in range(max(ids)):
            if i not in ids and i - 1 in ids and i + 1 in ids:
                return i


print(part2())
