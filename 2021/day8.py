def solve(lines):
    codes = get_codes(lines)
    return get_nb_1478(codes), get_total_sum(codes)


def get_nb_1478(codes):
    return sum(map(lambda c: sum(map(lambda x: c.count(x), '1478')), codes))


def get_total_sum(codes):
    return sum(map(lambda x: int(x), codes))


def has(haystack, needle):
    return all(map(lambda x: x in haystack, needle))


def get_code(line):
    patterns, cypher = line.split('|')
    patterns = patterns.split(' ')
    cypher = cypher.split(' ')

    one = next(filter(lambda x: len(x) == 2, patterns))
    four = next(filter(lambda x: len(x) == 4, patterns))
    seven = next(filter(lambda x: len(x) == 3, patterns))
    eight = next(filter(lambda x: len(x) == 7, patterns))
    six = next(filter(lambda x: len(x) == 6 and not(has(x, one)), patterns))
    patterns = [x for x in patterns if x not in [one, four, six, seven, eight]]
    nine = next(filter(lambda x: len(x) == 6 and has(x, four), patterns))
    patterns.remove(nine)
    zero = next(filter(lambda x: len(x) == 6, patterns))
    five = next(filter(lambda x: has(six, x) and has(nine, x), patterns))
    patterns = [x for x in patterns if x not in [zero, five]]
    three = next(filter(lambda x: has(x, one), patterns))
    patterns.remove(three)
    two = next(iter(patterns))

    ordered_patterns = [zero, one, two, three, four, five, six, seven, eight, nine]
    code = ''
    for x in cypher:
        for i in range(0, 10):
            digit = ordered_patterns[i]
            if len(x) == len(digit) and has(digit, x):
                code = f"{code}{i}"
    return code


def get_codes(lines):
    codes = []
    for l in lines:
        codes.append(get_code(l))
    return codes
