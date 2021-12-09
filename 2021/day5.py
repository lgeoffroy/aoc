import re

def solve(lines):
    return (compute(lines), compute(lines, True))


def get_dimensions(lines):
    x_max = 0
    y_max = 0
    for line in lines:
        x1, y1, x2, y2 = parse_line(line)
        x_max = max(x1, x2, x_max)
        y_max = max(y1, y2, y_max)
    return x_max, y_max


def parse_line(line):
    match = re.match(r'^(\d+),(\d+) -> (\d+),(\d+)$', line)
    x1, y1, x2, y2 = match.groups()
    return (int(x1), int(y1), int(x2), int(y2))


def compute(lines, with_diagonals = False):
    x_max, y_max = get_dimensions(lines)
    grid = [[0 for col in range(x_max + 1)] for row in range(y_max + 1)]
    for line in lines:
        x1, y1, x2, y2 = parse_line(line)
        if x1 == x2:
            ymin, ymax = (y1, y2) if y1 < y2 else (y2, y1)
            for y in range(ymin, ymax + 1):
                grid[y][x1] += 1
        elif y1 == y2:
            xmin, xmax = (x1, x2) if x1 < x2 else (x2, x1)
            for x in range(xmin, xmax + 1):
                grid[y1][x] += 1
        elif with_diagonals:
            i_sign = 1 if x1 < x2 else -1
            j_sign = 1 if y1 < y2 else -1
            diff = abs(x2 - x1)
            for i in range(diff + 1):
                grid[y1 + i * j_sign][x1 + i * i_sign] += 1
    nb = 0
    for row in grid:
        for elem in row:
            if elem > 1:
                nb += 1
    return nb
