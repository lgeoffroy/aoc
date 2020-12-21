def solve(input):
    space3 = parse_input(input, 3)
    space4 = parse_input(input, 4)
    for i in range(6):
        space3 = progress(space3, 3)
        space4 = progress(space4, 4)
    return (count_cubes(space3), count_cubes(space4))

def parse_input(input, dim):
    space = {}
    for i, line in enumerate(input):
        for j, symbol in enumerate(list(line)):
            if dim == 3:
                index = (i, j, 0)
            else:
                index = (i, j, 0, 0)
            space[index] = symbol == '#'
    return space

def progress(space, dim):
    new_space = {}
    (min_i, max_i, min_j, max_j, min_k, max_k, min_l, max_l) = get_boundaries(space, dim)
    for i in range(min_i-1, max_i+2):
        for j in range(min_j-1, max_j+2):
            for k in range(min_k-1, max_k+2):
                if dim == 4:
                    for l in range(min_l-1, max_l+2):
                        index = (i, j, k, l)
                        (n, neighbors) = get_neighbors(index, space, dim)
                        new_space[index] = n == 3 or (n == 2 and index in space and space[index])
                else:
                    index = (i, j, k)
                    (n, neighbors) = get_neighbors(index, space, dim)
                    new_space[index] = n == 3 or (n == 2 and index in space and space[index])
    return new_space

def get_boundaries(space, dim):
    if dim == 3:
        (min_i, min_j, min_k) = list(space.keys())[0]
        max_i, max_j, max_k = min_i, min_j, min_k
        min_l, max_l = 0, 0
    else:
        (min_i, min_j, min_k, min_l) = list(space.keys())[0]
        max_i, max_j, max_k, max_l = min_i, min_j, min_k, min_l

    for index in space.keys():
        if dim == 3:
            (i, j, k) = index
        else:
            (i, j, k, l) = index
        if i < min_i:
            min_i = i
        if j < min_j:
            min_j = j
        if k < min_k:
            min_k = k
        if dim == 4 and l < min_l:
            min_l = l
        if i > max_i:
            max_i = i
        if j > max_j:
            max_j = j
        if k > max_k:
            max_k = k
        if dim == 4 and l > max_l:
            max_l = l
    return (min_i, max_i, min_j, max_j, min_k, max_k, min_l, max_l)

def get_neighbors(index, space, dim):
    if dim == 3:
        (i, j, k) = index
    else:
        (i, j, k, l) = index
    neighbors = {}
    for x in [i-1, i, i+1]:
        for y in [j-1, j, j+1]:
            for z in [k-1, k, k+1]:
                if dim == 4:
                    for w in [l-1, l, l+1]:
                        index = (x, y, z, w)
                        if index != (i, j, k, l):
                            neighbors[index] = space[index] if index in space else False
                else:
                    index = (x, y, z)
                    if index != (i, j, k):
                        neighbors[index] = space[index] if index in space else False
    return (count_cubes(neighbors), neighbors)

def count_cubes(space):
    n = 0
    for i in space.values():
        if i:
            n += 1
    return n
