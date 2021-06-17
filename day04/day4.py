import re


def part1():
    with open("input.txt", "r") as f:
        line = f.readline()
        count = 0

        attrs = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False}

        while line:
            line = line.strip()
            if line == "":
                if all(attrs.values()):
                    count += 1

                attrs = dict.fromkeys(attrs, False)
            else:
                pairs = line.split()

                for pair in pairs:
                    [key, _] = pair.split(":")

                    if key == "cid":
                        continue

                    attrs[key] = True

            line = f.readline()

        return count


def part2():
    with open("input.txt", "r") as f:
        line = f.readline()
        count = 0

        attrs = {"byr": '', "iyr": '', "eyr": '', "hgt": '', "hcl": '', "ecl": '', "pid": ''}

        while line:
            line = line.strip()
            if line == "":
                if valid(attrs):
                    count += 1

                attrs = dict.fromkeys(attrs, '')
            else:
                pairs = line.split()

                for pair in pairs:
                    [key, val] = pair.split(":")

                    if key == "cid":
                        continue

                    attrs[key] = val

            line = f.readline()

        return count


def valid(attrs):
    try:
        if not (1920 <= int(attrs['byr']) <= 2002
                and 2010 <= int(attrs['iyr']) <= 2020
                and 2020 <= int(attrs['eyr']) <= 2030):
            return False

        if "cm" in attrs['hgt']:
            if not 150 <= int(attrs['hgt'][:-2]) <= 193:
                return False
        elif "in" in attrs['hgt']:
            if not 59 <= int(attrs['hgt'][:-2]) <= 79:
                return False
        else:
            return False

        p = re.compile("#[a-z0-9]{6}$")

        if not p.match(attrs['hcl']):
            return False

        colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if not attrs['ecl'] in colours:
            return False

        p = re.compile("[0-9]{9}$")

        if not p.match(attrs['pid']):
            return False

        return True
    except:
        return False


print(part2())
