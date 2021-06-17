import copy
import math

def main():
    rule_names = []
    rules = []
    my_values = []
    valid_values = []
    with open("input.txt", "r") as f:
        line = f.readline().strip()
        while line:
            [name, ranges] = line.split(":")
            ranges = ranges.strip().split("or")

            temp = []
            for fooRange in ranges:
                temp.append(tuple(map(int, fooRange.strip().split("-"))))

            rule_names.append(name)
            rules.append(temp)
            line = f.readline().strip()

        f.readline()
        my_values = list(map(int, f.readline().strip().split(",")))

        f.readline()
        f.readline()

        valid_values = []
        line = f.readline().strip()

        while line:
            values = list(map(int, line.split(",")))
            if is_values_valid(values, rules):
                valid_values.append(values)
            line = f.readline().strip()

    possible_indexes = [list(range(len(my_values))) for _ in rule_names]

    for values in valid_values:
        # values = [3,9,18]
        for j, ranges in enumerate(rules):
            # ranges = 0-1, 4-19
            for k, index in enumerate(possible_indexes[j]):
                # index = 0
                value = values[index]

                if not check_value_against_rule(value, ranges):
                    possible_indexes[j][k] = None

            possible_indexes[j] = [i for i in possible_indexes[j] if i is not None]

    new_indexes = []
    allocation = [-1 for _ in rule_names]
    taken = set()
    while new_indexes != possible_indexes:
        new_indexes = copy.deepcopy(possible_indexes)
        for i, indexes in enumerate(new_indexes):
            if len(indexes) == 1:
                allocation[i] = indexes[0]
                taken.add(indexes[0])

        for i, indexes in enumerate(new_indexes):
            if len(indexes) > 1 and not set(indexes).isdisjoint(taken):
                possible_indexes[i] = list(set(indexes) - taken)

    print(allocation)

    indexes_to_add = [allocation[i] for i, name in enumerate(rule_names) if name.startswith("departure")]

    print(indexes_to_add)

    print(math.prod([my_values[i] for i in indexes_to_add]))


def is_values_valid(values, rules):
    for value in values:
        if not is_single_value_valid(value, rules):
            return False

    return True


def is_single_value_valid(value, rules):
    for ranges in rules:
        if check_value_against_rule(value, ranges):
            return True

    return False


def check_value_against_rule(value, ranges):
    for (start, end) in ranges:
        if value in range(start, end + 1):
            return True

    return False


if __name__ == "__main__":
    main()
