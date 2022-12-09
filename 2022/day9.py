def move_head(h, direction):
    hx, hy = h[0], h[1]
    if direction == "U":
        return (hx, hy + 1)
    if direction == "D":
        return (hx, hy - 1)
    if direction == "L":
        return (hx - 1, hy)
    if direction == "R":
        return (hx + 1, hy)


def move_tail(rope):
    for i in range(len(rope) - 1):
        hx, hy = rope[i]
        tx, ty = rope[i + 1]
        if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
            continue
        if hx == tx:
            rope[i + 1] = tx, ty + (1 if hy - ty > 0 else -1)
        elif hy == ty:
            rope[i + 1] = tx + (1 if hx - tx > 0 else -1), ty
        else:
            rope[i + 1] = tx + (1 if hx - tx > 0 else -1), ty + (
                1 if hy - ty > 0 else -1
            )
    return rope


def apply_moves(lines, rope):
    visited = set([rope[-1]])
    for line in lines:
        direction, moves = line.split(" ")
        for _ in range(int(moves)):
            rope[0] = move_head(rope[0], direction)
            for _ in range(len(rope) - 1):
                rope = move_tail(rope)
            visited.add(rope[-1])
    return len(visited)


def solve(lines):
    return apply_moves(lines, [(0, 0)] * 2), apply_moves(lines, [(0, 0)] * 10)
