from functools import reduce


def solve(lines):
    low_points = get_low_points(lines)

    basin_sizes = []
    for _, x, y in low_points:
        basin_sizes.append(len(get_basin(lines, x, y)))
    basin_sizes.sort()

    lvl1 = sum(map(lambda x: x[0], low_points)) + len(low_points)
    lvl2 = reduce(lambda x, y: x * y, basin_sizes[-3:], 1)

    return lvl1, lvl2


def is_low_point(middle, dirs):
    return all(map(lambda x: x > middle, dirs))


def get_left(lines, i, j):
    return 9 if j == 0 else int(lines[i][j-1])
def get_right(lines, i, j):
    return 9 if j == len(lines[i]) - 1 else int(lines[i][j+1])
def get_down(lines, i, j):
    return 9 if i == 0 else int(lines[i-1][j])
def get_up(lines, i, j):
    return 9 if i == len(lines) - 1 else int(lines[i+1][j])


def get_low_points(lines):
    low_points = []
    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            middle = int(val)
            left = get_left(lines, i, j)
            right = get_right(lines, i, j)
            down = get_down(lines, i, j)
            up = get_up(lines, i, j)
            if is_low_point(middle, [left, right, down, up]):
                low_points.append((middle, i, j))
    return low_points


def get_basin(lines, x, y):
    points_in_basin = [(x, y)]

    def explore(lines, i, j):
        for di, dj, get_close in [
            (0, -1, get_left),
            (0, 1, get_right),
            (-1, 0, get_down),
            (1, 0, get_up),
        ]:
            if (i + di, j + dj) not in points_in_basin and get_close(lines, i, j) != 9:
                points_in_basin.append((i + di, j + dj))
                explore(lines, i + di, j + dj)

    explore(lines, x, y)

    return points_in_basin
