import re
from utils import get_level_input

def solve():
    input = get_level_input(2)
    lines = input.splitlines()
    valid1 = 0
    valid2 = 0

    for line in lines:
        match = re.match('^(\d+)-(\d+) (\w): (\w+)$', line)
        (n, m, l, passwd) = match.groups()
        count = passwd.count(l)
        if count >= int(n) and count <= int(m):
            valid1 += 1
        if (passwd[int(n) - 1] == l) ^ (passwd[int(m) - 1] == l):
            valid2 += 1

    return (valid1, valid2)
