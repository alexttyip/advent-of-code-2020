def main():
    rules = []
    with open("input.txt", "r") as f:
        line = f.readline().strip()
        while line:
            rule = line.split(": ")[1]
            rule = rule.split(" or ")

            temp = []
            for fooRange in rule:
                temp.append(tuple(map(int, fooRange.split("-"))))

            rules.append(temp)

            line = f.readline().strip()

        f.readline()
        values = f.readline().strip().split(",")

        rate = check_values(values, rules)

        f.readline()
        f.readline()
        line = f.readline().strip()

        while line:
            values = line.split(",")
            rate += check_values(values, rules)
            line = f.readline().strip()

        print(rate)


def check_values(values, rules):
    rate = 0
    for value in map(int, values):
        valid = False
        for rule in rules:
            # foo_valid = False
            for (start, end) in rule:
                if value in range(start, end + 1):
                    # foo_valid = True
                    valid = True

            # valid = foo_valid

        if not valid:
            rate += value

    return rate


if __name__ == "__main__":
    main()
