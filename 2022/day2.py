from functools import reduce


def solve(lines):
    order_lvl1 = ["B X", "C Y", "A Z", "A X", "B Y", "C Z", "C X", "A Y", "B Z"]
    order_lvl2 = ["B X", "C X", "A X", "A Y", "B Y", "C Y", "C Z", "A Z", "B Z"]
    return (
        reduce(lambda acc, line: acc + order_lvl1.index(line) + 1, lines, 0),
        reduce(lambda acc, line: acc + order_lvl2.index(line) + 1, lines, 0),
    )
