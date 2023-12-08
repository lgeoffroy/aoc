def lvl1(line):
    digits = [x for x in line if x in "0123456789"]
    return int(f"{digits[0]}{digits[-1]}")


def lvl2(line):
    d1, d2 = None, None
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for i, x in enumerate(line):
        if x in "0123456789":
            d1 = x
        for number in numbers:
            if d1 is None and line[i:].startswith(number):
                d1 = numbers[number]
        if d1 is not None:
            break
    for i, x in enumerate(reversed(line)):
        if x in "0123456789":
            d2 = x
        for number in numbers:
            if d2 is None and line[len(line) - i - 1 :].startswith(number):
                d2 = numbers[number]
        if d2 is not None:
            break
    return int(f"{d1}{d2}")


def solve(lines):
    return sum([lvl1(line) for line in lines]), sum([lvl2(line) for line in lines])
