def part1():
    with open("input.txt", "r") as f:
        return run(f.read().splitlines())[1]


def run(commands):
    acc = 0
    curr = 0

    hist = []

    while curr not in hist and curr < len(commands):
        hist.append(curr)

        opc = commands[curr][:3]
        ope = int(commands[curr][4:])

        if opc == "nop":
            curr += 1
            continue

        if opc == "acc":
            acc += ope
            curr += 1
            continue

        if opc == "jmp":
            curr += ope
            continue

    return curr, acc


def part2():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

        (curr, acc) = run(lines)

        if curr == len(lines):
            return acc

        for i in range(len(lines)):
            temp = lines.copy()
            line = temp[i]

            if 'acc' in line:
                continue

            if 'jmp' in line:
                temp[i] = line.replace('jmp', 'nop')
            else:
                temp[i] = line.replace('nop', 'jmp')

            (curr, acc) = run(temp)

            if curr == len(lines):
                return acc


print(part2())
