import re

def solve(lines):
    points = []
    instructions = []

    for line in lines:
        match = re.match(r'^(\d+),(\d+)$', line)
        if not match:
            match = re.match(r'^fold along (\w)=(\d+)$', line)
            if match:
                axis, n = match.groups()
                instructions.append((axis, int(n)))
        else:
            x, y = match.groups()
            points.append([int(x), int(y)])

    def fold(points, axis, n):
        coord = 0 if axis == "x" else 1
        new_points = []
        for point in points:
            new_point = list(point)
            if point[coord] > n:
                new_point[coord] = n - (point[coord] - n)
                new_points.append(new_point)
            else:
                new_points.append(point)
        final_points = []
        for point in new_points:
            if point not in final_points:
                final_points.append(point)
        return final_points


    points = fold(points, *instructions[0])
    points_lvl1 = list(points)
    for x in instructions[1:]:
        points = fold(points, *x)

    display_points(points)

    return len(points_lvl1) # level2 is just reading the displayed text

def display_points(points):
    xmax = max(map(lambda x: x[0], points))
    ymax = max(map(lambda x: x[1], points))
    for i in range(ymax+1):
        for j in range(xmax+1):
            if [j, i] in points:
                print("#", end="")
            else:
                print(" ", end="")
        print("")
    print("")
