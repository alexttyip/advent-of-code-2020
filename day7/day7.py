import re


def part1():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

        bags = {}

        for line in lines:
            p = re.compile(r'([a-z ]*) bags contain ')
            m = p.match(line)
            parent = m.group(1)

            line = line[m.end():]

            if line == "no other bags.":
                continue

            p = re.compile(r'[0-9]* ([a-z ]+) bags?(?:, |.)?')

            while line:
                m = p.match(line)
                name = m.group(1)

                if name in bags:
                    bags[name].append(parent)
                else:
                    bags[name] = [parent]

                line = line[m.end():]

        target = "shiny gold"
        counted = []
        uncounted = []
        if target in bags:
            uncounted = bags[target]

        while uncounted:
            bag = uncounted.pop(0)
            if bag not in counted:
                counted.append(bag)
                if bag in bags:
                    uncounted.extend(bags[bag])

        return len(counted)


def part2():
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()

        bags = {}

        for line in lines:
            p = re.compile(r'([a-z ]*) bags contain ')
            m = p.match(line)
            parent = m.group(1)

            line = line[m.end():]

            if line == "no other bags.":
                bags[parent] = []
                continue

            children = []
            p = re.compile(r'([0-9]*) ([a-z ]+) bags?(?:, |.)?')

            while line:
                m = p.match(line)
                num = m.group(1)
                child = m.group(2)

                children.append((child, int(num)))
                line = line[m.end():]

            bags[parent] = children
        return count(bags, "shiny gold") - 1


def count(bags, root):
    if root not in bags or bags[root] == []:
        return 1

    ans = 0

    children = bags[root]
    for (bag, num) in children:
        ans += count(bags, bag) * num

    return ans + 1


# class Bag:
#     def __init__(self, name, parent):
#         self.name = name
#         self.parent = parent


print(part2())
