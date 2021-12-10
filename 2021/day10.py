from functools import reduce
from statistics import median


def solve(lines):
    return lvl1(lines), lvl2(lines)


def invert(x):
    return {
        "]": "[",
        "}": "{",
        ")": "(",
        ">": "<",
    }[x]


def get_score(x):
    return {
        "]": 57,
        "[": 2,
        "}": 1197,
        "{": 3,
        ")": 3,
        "(": 1,
        ">": 25137,
        "<": 4,
    }[x] if x else 0


def get_first_invalid_character(line):
    stack = []
    for x in line:
        if x in "[{(<":
            stack.append(x)
        else:
            if stack[-1] != invert(x):
                return x
            stack.pop()
    return None


def lvl1(lines):
    return reduce(lambda acc, x: acc + get_score(get_first_invalid_character(x)), lines, 0)


def get_closing_sequence_score(line):
    stack = []
    for x in line:
        if x in "[{(<":
            stack.append(x)
        else:
            stack.pop()
    return reduce(lambda acc, x: acc*5 + get_score(x), reversed(stack), 0)


def lvl2(lines):
    incompletes = filter(lambda x: get_score(get_first_invalid_character(x)) == 0, lines)
    return median(map(get_closing_sequence_score, incompletes))

