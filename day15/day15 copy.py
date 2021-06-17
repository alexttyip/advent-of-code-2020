numbers = [8, 11, 0, 19, 1, 2]
# numbers = [0, 3, 6]


def part1():
    turn = len(numbers) - 1
    val = numbers[turn]

    while turn < 30000000:
    # while turn < 2020:
        found = False
        i = turn - 1
        val = numbers[turn]

        while i >= 0 and not found:
            if numbers[i] == val:
                found = True
            else:
                i -= 1

        if found:
            numbers.append(turn - i)
        else:
            numbers.append(0)

        turn += 1

    return numbers[-2]
    # dict = {num: turn+1 for (turn, num) in enumerate(starting_numbers)}
    # turn = len(starting_numbers) + 2
    # val = 0

    # while turn <= 30000000:
    #     if val in dict:
    #         temp = turn - 1 - dict[val]
    #     else:
    #         temp = 0

    #     dict[val] = turn - 1
    #     val = temp
    #     turn += 1

    # return val


print(part1())
