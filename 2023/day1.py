def reduce_line(line):
    digits = [x for x in line if x in "0123456789"]
    try:
        return int(f"{digits[0]}{digits[-1]}")
    except ValueError:
        print(line)
        raise
    except IndexError:
        print(line)
        raise


def reduce_line_corrected(line):
    new_line = ""
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
    i = 0
    while i < len(line):
        copy = True
        for number in numbers:
            if copy and line[i:].startswith(number):
                new_line += numbers[number]
                i += len(number)
                copy = False
                break
        if copy:
            new_line += line[i]
            i += 1
    print(new_line)
    return reduce_line(new_line)


def solve(lines):
    return sum([reduce_line(line) for line in lines]), sum(
        [reduce_line_corrected(line) for line in lines]
    )
