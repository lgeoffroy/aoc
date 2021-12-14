import re

def solve(lines):
    polymer = lines[0]
    instructions = {}
    for line in lines[2:]:
        match = re.match(r'^(\w{2}) -> (\w)$', line)
        pair, insert = match.groups()
        instructions[pair] = insert
    repartition = build_repartition(polymer, instructions)
    for _ in range(10):
        repartition = step(instructions, repartition)
    lvl1 = get_answer(polymer, repartition)
    for _ in range(30):
        repartition = step(instructions, repartition)
    lvl2 = get_answer(polymer, repartition)
    return lvl1, lvl2


def get_answer(polymer, repartition):
    letters = set([item for sublist in map(lambda x: list(x), repartition.keys()) for item in sublist])
    letter_occurences = {l: 0 for l in letters}
    for key in repartition:
        l1, l2 = tuple(key)
        letter_occurences[l1] += repartition[key] # each will be counted twice, apart from the first and last letter (which never change)
        letter_occurences[l2] += repartition[key]
    letter_occurences[polymer[0]] += 1
    letter_occurences[polymer[-1]] += 1
    return (max(letter_occurences.values()) - min(letter_occurences.values())) // 2


def build_repartition(polymer, instructions):
    binomes = {}
    letters = []
    for pair in list(instructions.keys()) + list(instructions.values()):
        letters += list(pair)
    letters = set(letters)
    for l1 in letters:
        for l2 in letters:
            binomes[f"{l1}{l2}"] = 0
    for i in range(len(polymer) - 1):
        binomes[f"{polymer[i]}{polymer[i+1]}"] += 1
    return binomes


def step(instructions, repartition):
    new_repartition = dict(repartition)
    for key, val in ((k, v) for k, v in repartition.items() if v > 0):
        l1, l2 = tuple(key)
        l = instructions[key]
        b1, b2 = f"{l1}{l}", f"{l}{l2}"
        new_repartition[key] -= val
        new_repartition[b1] += val
        new_repartition[b2] += val
    return new_repartition

