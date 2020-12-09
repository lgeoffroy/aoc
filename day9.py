def solve(input):
    values = [int(x) for x in input]
    invalid_value = part1(values)
    return (invalid_value, part2(values, invalid_value))

def part1(values):
    i = 0
    while True:
        tail = values[i:i+25]
        acc = values[i+25]
        is_valid = False
        for x in tail:
            for y in tail:
                if x + y == acc:
                    is_valid = True
        if not is_valid:
            return acc
        i += 1

def part2(values, invalid_value):
    for i in range(len(values)):
        j = 2
        acc = 0
        while acc < invalid_value:
            subset = values[i:i+j]
            acc = sum(subset)
            if acc == invalid_value:
                return min(subset) + max(subset)
            j += 1
