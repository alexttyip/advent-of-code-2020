def part1():
    with open("input.txt", "r") as f:
        line = f.readline()
        count = 0

        questions = set(())

        while line:
            line = line.strip()
            if line == "":
                count += len(questions)
                questions = set(())
            else:
                for char in line:
                    questions.add(char)
            line = f.readline()

        return count + len(questions)


def part2():
    with open("input.txt", "r") as f:
        line = f.readline()
        ans = 0
        pax_count = 0
        questions = {}

        while line:
            line = line.strip()
            if line == "":
                ans += len([v for v in questions.values() if v == pax_count])
                print(len([v for v in questions.values() if v == pax_count]))
                pax_count = 0
                questions = {}
            else:
                for char in line:
                    if char in questions:
                        questions[char] += 1
                    else:
                        questions[char] = 1

                pax_count += 1

            line = f.readline()

        if pax_count != 0:
            if all([v == pax_count for v in questions.values()]):
                ans += pax_count

        return ans


print(part2())
