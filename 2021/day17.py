import re

def solve(lines):
    match = re.match(r'^target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)$', lines[0])
    x_min, x_max, y_min, y_max = match.groups()
    x_min, x_max, y_min, y_max = int(x_min), int(x_max), int(y_min), int(y_max)

    vx, vy = find_initial_velocity(x_min, x_max, y_min, y_max)
    velocities = find_initial_velocity(x_min, x_max, y_min, y_max, False)
    return find_highest_position(vx, vy), len(velocities)


def find_initial_velocity(x_min, x_max, y_min, y_max, only_first=True):
    all_velocities = []
    for vy in range(300, y_min-1, -1):
        for vx in range(0, x_max+1, 1 if x_max > 0 else -1):
            if check_solution(vx, vy, x_min, x_max, y_min, y_max):
                if only_first:
                    return vx, vy
                all_velocities.append((vx, vy))
    return all_velocities


def find_highest_position(vx, vy):
    y_max = 0
    x, y = 0, 0
    while True:
        x, y, vx, vy = step(x, y, vx, vy)
        if y > y_max:
            y_max = y
        else:
            return y_max


def step(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    if vx < 0:
        vx += 1
    vy -= 1
    return x, y, vx, vy


def check_solution(vx, vy, x_min, x_max, y_min, y_max):
    x, y = 0, 0
    while True:
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True
        if y < y_min and vy < 0:
            return False
        if vx > 0 and x > x_max or vx < 0 and x < x_min:
            return False
        x, y, vx, vy = step(x, y, vx, vy)
