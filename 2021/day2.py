import re

def solve(lines):
    return (lvl1(lines), lvl2(lines))


def lvl1(lines):
    x, z = 0, 0
    for line in lines:
        match = re.match(r'^(\w+) (\d+)$', line)
        dir, step = match.groups()
        step = int(step)
        if dir == 'forward':
            x += step
        elif dir == 'down':
            z += step
        elif dir == 'up':
            z -= step

    return x * z


def lvl2(lines):
    x, z, a = 0, 0, 0
    for line in lines:
        match = re.match(r'^(\w+) (\d+)$', line)
        dir, step = match.groups()
        step = int(step)
        if dir == 'forward':
            x += step
            z += a * step
        elif dir == 'down':
            a += step
        elif dir == 'up':
            a -= step

    return x * z
