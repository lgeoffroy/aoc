import functools

def solve(lines):
    input = lines[0].split(",")

    for i in range(len(input)):
        input[i] = int(input[i])

    return (compute(input, 1), compute(input, 2))

def distance(element, target, lvl):
    d = abs(element - target)
    if lvl == 1:
        return d
    else:
        return d * (d + 1) // 2

def mesure(input, val, lvl):
    return functools.reduce(lambda acc, el: acc + distance(el, val, lvl), input, 0)


def compute(input, lvl):
    left = min(input)
    right = max(input)
    current = (right - left) // 2

    while True:
        left_d = mesure(input, left, lvl)
        right_d = mesure(input, right, lvl)

        if abs(current - left) == 1:
            return min(mesure(input, current, lvl), left_d)
        if abs(current - right) == 1:
            return min(mesure(input, current, lvl), right_d)

        if left_d > right_d:
            left = current
        else:
            right = current
        current = (right + left) // 2
