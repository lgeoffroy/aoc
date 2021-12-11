def solve(lines):
    input = []
    for line in lines:
        input.append(list(map(lambda x: int(x), line)))

    flashes = 0
    n = 0
    while True:
        n += 1
        if n <= 100:
            flashes += advance_step(input)
        else:
            x = advance_step(input)
            if x == 100:
                return flashes, n


def increase_neighbors(lines, i, j):
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == dj and di == 0:
                continue
            if i+di < 0 or j+dj < 0:
                continue
            try:
                if lines[j+dj][i+di] != 0:
                    lines[j+dj][i+di] += 1
            except IndexError:
                continue
    return lines


def must_flash(lines):
    return any(map(lambda line: any(map(lambda x: x > 9, line)), lines))


def flash(lines):
    flashes = 0
    copy = [x[:] for x in lines]
    for j, line in enumerate(copy):
        for i, x in enumerate(line):
            if x > 9:
                increase_neighbors(lines, i, j)
                lines[j][i] = 0
                flashes += 1
    return flashes


def advance_step(lines):
    for line in lines:
        for i, x in enumerate(line):
            line[i] = x + 1
    flashes = 0
    while must_flash(lines):
        flashes += flash(lines)
    return flashes
