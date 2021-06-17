import math
from functools import reduce


def part1():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        earliest = int(lines[0])
        buses = sorted([int(v) for v in lines[1].split(',') if v != 'x'])
        diff = []
        for bus in buses:
            bus = bus * (earliest // bus + 1)
            # while bus < earliest:
            # bus += bus

            diff.append(bus - earliest)

        min_diff = min(diff)

        return buses[diff.index(min_diff)] * min_diff


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def part2():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        line = lines[1].split(',')
        n = []
        a = []

        for i in range(len(line)):
            if line[i] != 'x':
                n.append(int(line[i]))
                a.append(int(line[i]) - i)

        return chinese_remainder(n, a)

        # N = reduce(lambda acc, curr: acc * curr, n, 1)

        # result = 0
        # for i in range(len(n)):
        #     ai = a[i]
        #     ni = n[i]
        #     bi = N // ni
        #     result += ai * bi * invmod(bi, ni)

        # result = result % N

        # return result
        # found = False
        # t = 0
        # while not found:
        #     found = True
        #     t += buses[0]

        #     for i in range(1, len(buses)):
        #         bus = buses[i]
        #         offset = offsets[i]

        #         if (t + offset) % bus != 0:
        #             found = False
        #             break

        # return t


print(part2())
