def solve(lines):
    total_lvl1 = 0
    total_lvl2 = 0
    for line in lines:
        [pair1, pair2] = line.split(",")
        [a, b, c, d] = map(lambda x: int(x), pair1.split("-") + pair2.split("-"))
        if c <= a <= d and c <= b <= d or a <= c <= b and a <= d <= b:
            total_lvl1 += 1
        if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
            total_lvl2 += 1
    return total_lvl1, total_lvl2
