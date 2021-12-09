def solve(lines):
    adapters = [0] + [int(x) for x in lines]
    adapters.sort()
    adapters.append(adapters[-1] + 3)
    return (part1(adapters), part2(adapters))

def part1(adapters):
    ones = 0
    threes = 0
    for i in range(1, len(adapters)):
        if adapters[i] - adapters[i-1] == 1:
            ones += 1
        elif adapters[i] - adapters[i-1] == 3:
            threes += 1
    return ones * threes

def cut(adapters, n):
    i = 0
    while adapters[i] != n:
        i += 1
    return adapters[i:]

results = {1: 1, 2: 1, 3: 1}

def part2(adapters):
    try:
        return results[len(adapters)]
    except KeyError:
        first = adapters[0]
        n = 0
        if first + 1 in adapters:
            n += part2(cut(adapters, first + 1))
        if first + 2 in adapters:
            n += part2(cut(adapters, first + 2))
        if first + 3 in adapters:
            n += part2(cut(adapters, first + 3))
        results[len(adapters)] = n
        return n
