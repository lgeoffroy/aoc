import re

def solve(lines):
    valid1 = 0
    valid2 = 0

    for line in lines:
        match = re.match(r'^(\d+)-(\d+) (\w): (\w+)$', line)
        (n, m, l, passwd) = match.groups()
        count = passwd.count(l)
        if count >= int(n) and count <= int(m):
            valid1 += 1
        if (passwd[int(n) - 1] == l) ^ (passwd[int(m) - 1] == l):
            valid2 += 1

    return (valid1, valid2)
