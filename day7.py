import regex
from utils import get_level_input

def solve():
    input = get_level_input(7)
    rules = input.splitlines()
    valid_colors = []

    def add_color_from_rule(rule):
        match = regex.match(r'^(\w+) (\w+) bags? contain', rule)
        matches = match.groups()
        color = (matches[0], matches[1])
        if color not in valid_colors:
            valid_colors.append(color)

    for rule in rules:
        if regex.search(r'contain.*shiny gold bag', rule):
            add_color_from_rule(rule)

    while True:
        original_length = len(valid_colors)
        for valid in valid_colors:
            for rule in [x for x in rules \
                    if regex.search('contain.*' + valid[0] + ' ' + valid[1], x) is not None]:
                add_color_from_rule(rule)
        if original_length == len(valid_colors):
            part1 = original_length
            break

    for rule in rules:
        if regex.search(r'^shiny gold bags contain', rule) is not None:
            start_rule = rule

    def count_bags(partial_rule):
        start_rule = None

        for rule in rules:
            if regex.search(partial_rule, rule) is not None:
                start_rule = rule

        if regex.search(r'.*no other bag', start_rule):
            return 1

        match = regex.match(r'.*contains?( (\d+) (\w+) (\w+) bags?,?)+', start_rule)
        numbers = match.captures(2)
        adjs = match.captures(3)
        colors = match.captures(4)

        sum = 0
        for i in range(len(numbers)):
            next_partial_rule = '^' + adjs[i] + ' ' + colors[i] + ' bags contain'
            nb_inside_bags = count_bags(next_partial_rule)
            sum += int(numbers[i]) * nb_inside_bags

        return sum + 1 # count current containing bag

    part2 = count_bags(r'^shiny gold bags contain') - 1 # don't count shiny gold bag

    return (part1, part2)
