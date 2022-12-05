def parse_lines(lines):
    i = lines.index("")
    stack_data, instructions = lines[:i], lines[i + 1 :]
    maxlen = len(max(stack_data, key=len))
    stack_data = [x + (" " * (maxlen - len(x))) for x in stack_data]
    stack_data = list(
        map(lambda x: list("".join(reversed(list(x))).strip()), zip(*stack_data[:-1]))
    )[1::4]
    return stack_data, instructions


def lvl1(lines):
    stacks, instructions = parse_lines(lines)
    for instruction in instructions:
        _, n, _, start, _, end = instruction.split(" ")
        for _ in range(int(n)):
            crate = stacks[int(start) - 1].pop()
            stacks[int(end) - 1].append(crate)

    return "".join([x[-1] for x in stacks])


def lvl2(lines):
    stacks, instructions = parse_lines(lines)
    for instruction in instructions:
        _, n, _, start, _, end = instruction.split(" ")
        crates = stacks[int(start) - 1][-int(n) :]
        stacks[int(end) - 1] += crates
        stacks[int(start) - 1] = stacks[int(start) - 1][: -int(n)]

    return "".join([x[-1] for x in stacks])


def solve(lines):
    return lvl1(lines), lvl2(lines)
