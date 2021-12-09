def solve(lines):
    return (lvl1(lines), lvl2(lines))


def get_number_of_ones(lines):
    line_size = len(lines[0])
    number_of_ones = [0] * line_size
    for line in lines:
        for i, b in enumerate(line):
            if b == '1':
                number_of_ones[i] += 1
    return number_of_ones


def lvl1(lines):
    number_of_ones = get_number_of_ones(lines)
    gamma_rate = 0
    epsilon_rate = 0
    for i, n in enumerate(reversed(number_of_ones)):
        if n > len(lines) / 2:
            gamma_rate += 2**i
        else:
            epsilon_rate += 2**i
    return gamma_rate * epsilon_rate


def reduce_rate(lines, is_oxygen, pos):
    if len(lines) == 1:
        return lines[0]
    number_of_ones = get_number_of_ones(lines)
    if is_oxygen:
        flt = '0' if number_of_ones[pos] >= len(lines) / 2 else '1'
    else:
        flt = '1' if number_of_ones[pos] >= len(lines) / 2 else '0'
    for i, l in enumerate(lines):
        if l[pos] == flt:
            lines[i] = None
    return reduce_rate(list(filter(None, lines)), is_oxygen, pos + 1)


def lvl2(lines):
    oxygen_rate = reduce_rate(list(lines), True, 0)
    co2_rate = reduce_rate(list(lines), False, 0)
    return int(oxygen_rate, 2) * int(co2_rate, 2)

