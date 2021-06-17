starting_numbers = [8, 11, 0, 19, 1, 2]
# starting_numbers = [2, 1, 3]


def part1():
    dict = {num: turn for (turn, num) in enumerate(starting_numbers, 1)}
    val = 23
    turn = 7
    dict[val], val = turn, 0 if val not in dict else turn - dict[val]
    print("hi")
    # for turn in range(len(starting_numbers) + 1, 2020):

    # turn = len(starting_numbers) + 2
    val = 0

    while turn <= 30000000:
        if val in dict:
            temp = turn - 1 - dict[val]
        else:
            temp = 0

        dict[val] = turn - 1
        val = temp
        turn += 1

    return val


print(part1())
