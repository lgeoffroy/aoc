def is_visible(grid, i, j):
    return any(
        (
            all(grid[x][j] < grid[i][j] for x in range(i)),
            all(grid[x][j] < grid[i][j] for x in range(i + 1, len(grid))),
            all(grid[i][y] < grid[i][j] for y in range(j)),
            all(grid[i][y] < grid[i][j] for y in range(j + 1, len(grid[i]))),
        )
    )


def scenic_score(grid, i, j):
    top, bottom, left, right = 0, 0, 0, 0
    stop, x = False, i
    while x > 0 and not stop:
        top += 1
        x -= 1
        if grid[x][j] >= grid[i][j]:
            stop = True
    stop, x = False, i
    while x < len(grid) - 1 and not stop:
        bottom += 1
        x += 1
        if grid[x][j] >= grid[i][j]:
            stop = True
    stop, y = False, j
    while y > 0 and not stop:
        left += 1
        y -= 1
        if grid[i][y] >= grid[i][j]:
            stop = True
    stop, y = False, j
    while y < len(grid[i]) - 1 and not stop:
        right += 1
        y += 1
        if grid[i][y] >= grid[i][j]:
            stop = True
    return top * bottom * left * right


def solve(lines):
    grid = [[x for x in line] for line in lines]
    return (
        sum(
            is_visible(grid, i, j)
            for i in range(len(grid))
            for j in range(len(grid[i]))
        ),
        max(
            scenic_score(grid, i, j)
            for i in range(1, len(grid) - 1)
            for j in range(1, len(grid[i]) - 1)
        ),
    )
