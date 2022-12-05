def solve(lines):
    def get_value(ascii_val):
        if ascii_val < 97:
            value = ascii_val - 38
        else:
            value = ascii_val - 96
        return value

    def get_doubles(bags):
        for bag in bags:
            half = int(len(bag) / 2)
            value = get_value(ord((set(bag[:half]) & set(bag[half:])).pop()))
            yield value

    def get_badges(bags):
        for bag1, bag2, bag3 in (bags[pos : pos + 3] for pos in range(0, len(bags), 3)):
            value = get_value(ord((set(bag1) & set(bag2) & set(bag3)).pop()))
            yield value

    return sum(get_doubles(lines)), sum(get_badges(lines))
