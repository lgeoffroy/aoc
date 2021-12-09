def solve(lines):
    product = 1

    for slope in [(1, 1), (5, 1), (7, 1), (1, 2), (3, 1)]:
        i = 0
        j = 0
        nb_trees = 0
        (y, x) = slope
        while i < len(lines):
            if lines[i][j] == '#':
                nb_trees += 1
            j += y
            if j >= len(lines[i]):
                j -= len(lines[i])
            i += x
        product *= nb_trees

    return (nb_trees, product)
