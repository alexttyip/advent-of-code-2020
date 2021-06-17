def find():
    f = open("input.txt", "r")

    numbers = [int(line) for line in f]
    numbers.sort()
    
    count = len(numbers)

    for i in range(count):
        I = numbers[i]
        for j in range(i, count):
            J = numbers[j]

            if I + J > 2020:
                break

            for k in range(j, count):
                K = numbers[k]

                if I + J + K == 2020:
                    return I * J * K
                elif I + J + K > 2020:
                    break

print(find())
