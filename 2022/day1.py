from functools import reduce


def solve(lines):
    calories = sorted(
        reduce(
            lambda x, y: x + [0] if y == "" else x[:-1] + [x[-1] + int(y)], lines, [0]
        ),
        reverse=True,
    )
    return calories[0], sum(calories[:3])
