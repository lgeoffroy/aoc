import math

def solve(lines):
    input = lines[0].split(",")

    for i in range(len(input)):
        input[i] = int(input[i])

    return (compute(input, 80), compute(input, 256))

def nb_descendants(x, n, dic):
    """Return nb of all descendants at year n of a fish reaching 0 for the first time on day x (0-index)"""
    if n <= x:
        return 0
    if x in dic:
        return dic[x]
    total = 0
    k = 0
    while x + k * 7 + 1 <= n:
        total += 1 + nb_descendants(x + k * 7 + 9, n, dic)
        k += 1
    dic[x] = total
    return total

def compute(input, n):
    total = len(input)
    dic = {}
    for x in input:
        total += nb_descendants(x, n, dic)
    return total
