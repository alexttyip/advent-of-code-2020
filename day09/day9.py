offset = 25


def part1():
    with open("input.txt", "r") as f:
        nums = list(map(int, f.read().splitlines()))
        i = 0

        mistake = -1

        while i + offset < len(nums) and mistake == -1:
            mistake = find_mistake(nums, i)
            i += 1

        return mistake


def find_mistake(nums, start):
    prev = sorted(nums[start: start + offset])
    target = nums[start + offset]

    for i in range(offset):
        foo_i = prev[i]

        if foo_i >= target:
            break

        if (target - foo_i) in prev[i + 1:]:
            return -1

    return target


def part2():
    with open("input.txt", "r") as f:
        nums = list(map(int, f.read().splitlines()))

        mistake = 36845998
        # mistake = 127

        (start, end) = find_range(nums, mistake, 0, 0)

        return min(nums[start:end]) + max(nums[start:end])


def find_range(nums, target, start, end):
    if start > end or end >= len(nums):
        return -1

    if sum(nums[start: end]) == target:
        return start, end

    if sum(nums[start: end]) < target:
        return find_range(nums, target, start, end + 1)

    if sum(nums[start: end]) > target:
        return find_range(nums, target, start + 1, end)


print(part2())
