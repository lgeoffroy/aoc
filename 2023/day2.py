import re


colors = ["blue", "red", "green"]


def id(line):
    return int(line[5 : line.index(":")])


def extract_subsets(line):
    sublines = line[line.index(":") + 1 :].split(";")
    subsets = []
    for subline in sublines:
        subset = {}
        for color in colors:
            search = re.findall(rf"(\d+) {color}", subline)
            if search:
                subset[color] = int(search[0])
        subsets.append(subset)
    return subsets


def is_possible(line, condition):
    subsets = extract_subsets(line)
    return all(
        all(
            subset.get(color, 0) <= condition[color] if color in condition else False
            for color in colors
        )
        for subset in subsets
        for subset in subsets
    )


def get_power(line):
    subsets = extract_subsets(line)
    power = 1
    for color in colors:
        power *= max(subset[color] if color in subset else 0 for subset in subsets)
    return power


def solve_lvl1(lines):
    condition = {
        "blue": 14,
        "green": 13,
        "red": 12,
    }
    return sum(id(line) for line in lines if is_possible(line, condition))


def solve_lvl2(lines):
    return sum(get_power(line) for line in lines)


def solve(lines):
    return solve_lvl1(lines), solve_lvl2(lines)
