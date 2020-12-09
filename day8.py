
import regex

def solve(lines):
    return (part1(lines), part2(lines))

def part1(lines, only_valid=False):
    instructions = lines[:]
    i = 0
    acc = 0
    while True:
        (op, val) = regex.match(r'^(\w+) ([+-]\d+)$', instructions[i]).groups()
        instructions[i] = 'loop +0'
        if op == 'acc':
            acc += int(val)
            i += 1
        elif op == 'nop':
            i += 1
        elif op == 'jmp':
            i += int(val)
        elif op == 'loop':
            return acc if not only_valid else False
        if i == len(instructions):
            return acc

def part2(lines):
    instructions = lines[:]
    i = 0
    acc = 0
    visited = []
    while True:
        (op, val) = regex.match(r'^(\w+) ([+-]\d+)$', instructions[i]).groups()
        instructions[i] = 'loop +0'
        if op != 'acc':
            visited.append(i)
        if op == 'acc' or op == 'nop':
            i += 1
        elif op == 'jmp':
            i += int(val)
        elif op == 'loop':
            break
    for i in visited:
        new_instructions = lines[:]
        (op, val) = regex.match(r'^(\w+) ([+-]\d+)$', instructions[i]).groups()
        new_instructions[i] = 'nop +0' if op == 'jmp' or val == '+0' else 'jmp ' + val
        res = part1(new_instructions, only_valid=True)
        if res != False:
            return res
