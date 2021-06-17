def part1():
    with open("input.txt", "r") as f:
        nums = list(map(int, f.read().splitlines()))

        nums = sorted(nums + [0, max(nums) + 3])

        diffs = {}

        # print(nums)

        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]

            # if diff == 3:
            # print(nums[i], nums[i+1])

            if diff in diffs:
                diffs[diff] += 1
            else:
                diffs[diff] = 1

        # print(diffs)
        return diffs[1] * diffs[3]


def part2():
    with open("input.txt", "r") as f:
        nums = list(map(int, f.read().splitlines()))

        nums = sorted(nums + [0, max(nums) + 3])

        acc = {key: 0 for key in nums}
        acc[max(nums)] = 1

        for i in range(len(nums) - 2, -1, -1):
            count = 0

            for j in range(1, 4):
                if nums[i] + j in nums:
                    acc[nums[i]] += acc[nums[i] + j]

        return acc[0]


print(part2())
