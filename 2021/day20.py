from itertools import product


def solve(lines):
    algorithm = lines[0]
    image = lines[2:]
    iterations = 50
    size_fill = iterations * 2
    x_max = len(image[0]) + size_fill * 2
    large_image = ["." * x_max] * size_fill
    fill = "".join(large_image[0][:size_fill])
    large_image += [f"{fill}{line}{fill}" for line in image]
    large_image += ["." * x_max] * size_fill
    for i in range(iterations):
        large_image = enhance(algorithm, large_image, i)
        if i == 1:
            lvl_1 = count_pixels(large_image)
    return lvl_1, count_pixels(large_image)


def count_pixels(image):
    return sum([line.count("#") for line in image])


def enhance(algorithm, image, i):
    return [
        "".join(
            [algorithm[get_index(x, y, image)] for y in range(1, len(image[0]) - 1)]
        ) for x in range(1, len(image) - 1)
    ]


def get_index(x, y, image):
    return int("".join(["1" if image[x+i][y+j] == "#" else "0" for i, j in product((-1,0,1), (-1,0,1))]), 2)
