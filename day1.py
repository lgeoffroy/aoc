def solve(lines):
    liste = [int(x) for x in lines]

    for i in liste:
        for j in liste:
            if i + j == 2020:
                part1 = i * j
            for k in liste:
                if i + j + k == 2020:
                    part2 = i * j * k

    return (part1, part2)
