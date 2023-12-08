SYMBOLS = "-*&$@/#=%+"
NUMBERS = "1234567890"


def get_neighbours(i, j):
    return [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]


def get_neighbourhood(lines, symbols=SYMBOLS):
    neighbourhood = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char in symbols:
                neighbourhood[i, j] = get_neighbours(i, j)
    return neighbourhood


def get_number(line, j):
    start, end = j, j
    while start > 0 and line[start - 1] in NUMBERS:
        start -= 1
    while end < len(line) - 1 and line[end + 1] in NUMBERS:
        end += 1
    return int(line[start : end + 1]), start


def lvl1(lines):
    n = len(lines)
    m = len(lines[0])
    neighbours = [x for list_x in get_neighbourhood(lines).values() for x in list_x]
    neighbourhood = set(
        [(i, j) for (i, j) in neighbours if 0 <= i <= n and 0 <= i <= m]
    )
    visited_positions = {}
    for i, j in neighbourhood:
        if lines[i][j] in NUMBERS:
            number, start_j = get_number(lines[i], j)
            if (i, start_j) in visited_positions:
                continue
            visited_positions[(i, start_j)] = number
    return sum(visited_positions.values())


def lvl2(lines):
    neighbourhood = get_neighbourhood(lines, symbols="*")
    sum = 0
    for pos, neighbours in neighbourhood.items():
        gear = {}
        for i, j in neighbours:
            if lines[i][j] in NUMBERS:
                number, start_j = get_number(lines[i], j)
                gear[i, start_j] = number
        if len(gear) == 2:
            gear_values = list(gear.values())
            sum += gear_values[0] * gear_values[1]
    return sum


def solve(lines):
    return lvl1(lines), lvl2(lines)
