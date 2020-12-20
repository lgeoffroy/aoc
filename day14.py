import regex

def solve(input):
    return (part1(input), part2(input))

def part1(input):
    mem = {}
    mask = None
    for line in input:
        match = regex.match(r'^mask = (\w+)$', line)
        if match:
            mask = match.groups()[0]
            continue
        match = regex.match(r'^mem\[(\d+)\] = (\d+)', line)
        (index, value) = match.groups()
        bin_value = bin(int(value))[2:].zfill(36)
        for i, bit in enumerate(mask):
            if bit != 'X':
                bin_value = bin_value[:i] + bit + bin_value[i+1:]
        mem[index] = int(bin_value, 2)
    return sum(mem.values())

def part2(input):
    mem = {}
    mask = None
    for line in input:
        match = regex.match(r'^mask = (\w+)$', line)
        if match:
            mask = match.groups()[0]
            continue
        match = regex.match(r'^mem\[(\d+)\] = (\d+)', line)
        (index, value) = match.groups()
        bin_index = bin(int(index))[2:].zfill(36)
        for i, bit in enumerate(mask):
            if bit != '0':
                bin_index = bin_index[:i] + bit + bin_index[i+1:]
        all_indexes = get_all_indexes(bin_index)
        for index in all_indexes:
            mem[index] = int(value)
    return sum(mem.values())

def get_all_indexes(bin_index):
    for i in range(len(bin_index)):
        if bin_index[i] == 'X':
            return get_all_indexes(bin_index[:i] + '0' + bin_index[i+1:]) \
                    + get_all_indexes(bin_index[:i] + '1' + bin_index[i+1:])
    return [bin_index]
