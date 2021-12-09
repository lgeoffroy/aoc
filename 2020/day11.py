import numpy as np
import warnings
import xxhash
warnings.simplefilter(action='ignore', category=FutureWarning)

def solve(input):
    grid = np.array(list(map(list, input)))
    (new_grid,hsh) = update(grid, False)

    return (run(grid, True), run(grid, False))

def run(grid, adjacent):
    oldhash = xxhash.xxh64(grid).hexdigest()
    while True:
        (grid, newhash) = update(grid, adjacent)
        if newhash == oldhash:
            return np.count_nonzero(grid == '#')
        oldhash = newhash

def update(grid, adjacent):
    (n, m) = grid.shape
    new_grid = np.copy(grid)
    max_to_leave = 4 if adjacent else 5
    for i in range(n):
        for j in range(m):
            nb_occupied = count_occupied(grid, i, j, adjacent)
            if grid[i][j] == 'L' and nb_occupied == 0:
                new_grid[i][j] = '#'
            elif grid[i][j] == '#' and nb_occupied >= max_to_leave:
                new_grid[i][j] = 'L'
    return (new_grid, xxhash.xxh64(new_grid).hexdigest())

def count_occupied(grid, i, j, adjacent):
    nb_occupied = 0
    (n, m) = grid.shape

    if adjacent:
        neighbors = grid[max(i-1,0):min(i+2,n), max(j-1,0):min(j+2,m)].flatten()
        nb_occupied = np.count_nonzero(neighbors == '#')
        return nb_occupied - 1 if grid[i][j] == '#' else nb_occupied

    # up
    if i > 0:
        for x in range(i-1, -1, -1):
            if grid[x][j] == '#':
                nb_occupied += 1
                break
            elif grid[x][j] == 'L':
                break
    # down:
    for x in range (i+1, n):
        if grid[x][j] == '#':
            nb_occupied += 1
            break
        elif grid[x][j] == 'L':
            break

    # left
    if j > 0:
        for y in range(j-1, -1, -1):
            if grid[i][y] == '#':
                nb_occupied += 1
                break
            elif grid[i][y] == 'L':
                break

    # right
    for y in range(j+1, m):
        if grid[i][y] == '#':
            nb_occupied += 1
            break
        elif grid[i][y] == 'L':
            break

    # diag up left
    if i > 0 and j > 0:
        x = 1
        while i-x >= 0 and j-x >= 0:
            if grid[i-x][j-x] == '#':
                nb_occupied += 1
                break
            elif grid[i-x][j-x] == 'L':
                break
            x += 1

    # diag up right
    if i > 0:
        x = 1
        while i-x >= 0 and j+x < m:
            if grid[i-x][j+x] == '#':
                nb_occupied += 1
                break
            elif grid[i-x][j+x] == 'L':
                break
            x += 1

    # diag down right
    x = 1
    while i+x < n and j+x < m:
        if grid[i+x][j+x] == '#':
            nb_occupied += 1
            break
        elif grid[i+x][j+x] == 'L':
            break
        x += 1

    # diag down left
    if j > 0:
        x = 1
        while i+x < n and j-x >= 0:
            if grid[i+x][j-x] == '#':
                nb_occupied += 1
                break
            elif grid[i+x][j-x] == 'L':
                break
            x += 1

    return nb_occupied
