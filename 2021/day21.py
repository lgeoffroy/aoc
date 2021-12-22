import re
from copy import deepcopy
from itertools import product

def solve(lines):
    players = []
    for line in lines:
        match = re.match(r'^Player \d+ starting position: (\d+)$', line)
        start, = match.groups()
        players.append({
            "position": int(start) - 1,
            "score": 0,
        })
    return play_deterministic(deepcopy(players)), play_dirac(players)


def generate_deterministic_dice():
    next_rolls = [1, 2, 3]
    while True:
        yield sum(next_rolls)
        next_rolls = [x+3 - 100 if x+3 > 100 else x+3 for x in next_rolls]


def play_deterministic(players):
    rolls = 0
    dice = generate_deterministic_dice()
    while not(any(map(lambda x: x["score"] >= 1000, players))):
        player = players[rolls%len(players)]
        player["position"] = (player["position"] + next(dice)) % 10
        rolls += 1
        player["score"] += player["position"] + 1
    return 3 * rolls * min(map(lambda x: x["score"], players))


def play_dirac(players):
    scores = {}
    for p in product([1,2,3], [1,2,3], [1,2,3]):
        if not sum(p) in scores:
            scores[sum(p)] = 0
        scores[sum(p)] += 1
    outcomes = [{
        (players[0]["position"], players[0]["score"]): 1,
    }, {
        (players[1]["position"], players[1]["score"]): 1,
    }]
    winning = [{}, {}]

    n = 0
    while outcomes[0] or outcomes[1]:
        for player in (0, 1):
            new_scores = {}
            for dice_score, nb in scores.items():
                for (pos, score), occurences in outcomes[player].items():
                    new_pos = (pos + dice_score) % 10
                    new_score = score + new_pos + 1
                    new_situation = (new_pos, new_score)
                    if new_score >= 21:
                        if n not in winning[player]:
                            winning[player][n] = 0
                        winning[player][n] += nb * occurences * sum(outcomes[player^1].values())
                    else:
                        if new_situation not in new_scores:
                            new_scores[new_situation] = 0
                        new_scores[new_situation] += nb*occurences
            outcomes[player] = new_scores
        n += 1

    return max((sum(x.values()) for x in winning))
