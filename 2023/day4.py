def str_to_int_list(str):
    return list(map(lambda x: int(x.strip()), (y for y in str.split(" ") if y != "")))


def lvl1(lines):
    total = 0
    for line in lines:
        winning, playing = list(
            map(str_to_int_list, line.split(":", 1)[1].split("|", 1))
        )
        if any(x in winning for x in playing):
            total += 2 ** (sum([True for x in playing if x in winning]) - 1)
    return total


def lvl2(lines):
    scores = {}
    for i, line in enumerate(lines):
        winning, playing = list(
            map(str_to_int_list, line.split(":", 1)[1].split("|", 1))
        )
        scores[i + 1] = sum([True for x in playing if x in winning])
    cards_to_scratch = {x: 1 for x in scores}
    score = len(lines)
    for i, line in enumerate(lines):
        for j in range(i + 2, i + 2 + scores[i + 1]):
            cards_to_scratch[j] += cards_to_scratch[i + 1]
        score += cards_to_scratch[i + 1] * scores[i + 1]
    return score


def solve(lines):
    return lvl1(lines), lvl2(lines)
