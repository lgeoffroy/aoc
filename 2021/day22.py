import re
import timeit

def solve(lines):
    actions = []
    for line in lines:
        match = re.match(r'^(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)$', line).groups()
        actions.append((match[0] == "on", tuple(int(x) for x in match[1:])))

    print(actions)
    return 0


def debug():
    print(solve([
        "on x=10..12,y=10..12,z=10..12",
        "on x=11..13,y=11..13,z=11..13",
        "off x=9..11,y=9..11,z=9..11",
        "on x=10..10,y=10..10,z=10..10",
    ]))

debug()


def update_on(on, action):
    pass

# on = []
# on = [10-12, 10-12, 10-12]
# on = [10-13, 10-13, 10-13]
# on = [12-13, 12-13, 12-13]
# on = [(10, 12-13), (10, 12-13), (10,12-13))]
