def solve(input):
    return (manhattan_distance(part1(input)), manhattan_distance(part2(input)))

def move_forward(position, direction, n):
    if direction == 'N':
        return (position[0] + n, position[1])
    if direction == 'E':
        return (position[0], position[1] + n)
    if direction == 'S':
        return (position[0] - n, position[1])
    if direction == 'W':
        return (position[0], position[1] - n)

def part1(input):
    position = (0, 0)
    direction = 'E'
    dirs = 'NESW'

    for instruction in input:
        letter = instruction[0]
        n = int(instruction[1:])
        if letter == 'F':
            position = move_forward(position, direction, n)
        if letter in dirs:
            position = move_forward(position, letter, n)
        if letter == 'L':
            i = dirs.index(direction)
            direction = dirs[(i - int(n/90)) % len(dirs)]
        if letter == 'R':
            i = dirs.index(direction)
            direction = dirs[(i + int(n/90)) % len(dirs)]

    return position

def part2(input):
    position = (0, 0)
    direction = 'E'
    waypoint = (1, 10)

    for instruction in input:
        letter = instruction[0]
        n = int(instruction[1:])
        if letter == 'F':
            for i in range(n):
                position = move_forward(position, 'N', waypoint[0])
                position = move_forward(position, 'E', waypoint[1])
        if letter == 'N':
            waypoint = (waypoint[0] + n, waypoint[1])
        if letter == 'E':
            waypoint = (waypoint[0], waypoint[1] + n)
        if letter == 'S':
            waypoint = (waypoint[0] - n, waypoint[1])
        if letter == 'W':
            waypoint = (waypoint[0], waypoint[1] - n)
        if letter in 'RL':
            if letter == 'R':
                waypoint = rotate_waypoint(waypoint, n)
            else:
                waypoint = rotate_waypoint(waypoint, -n)

    return position

def rotate_waypoint(waypoint, deg):
    rotation = deg
    new_waypoint = (waypoint[0], waypoint[1])
    if rotation < 0:
        rotation += 360
    while rotation > 0:
        new_waypoint = (-new_waypoint[1], new_waypoint[0])
        rotation -= 90
    return new_waypoint

def manhattan_distance(position):
    return abs(position[0]) + abs(position[1])
