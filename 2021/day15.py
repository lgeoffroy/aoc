from math import inf

def solve(lines):
    graph = parse_graph(lines)
    s_deb = graph["S"][0]
    s_fin = graph["S"][-1]
    predecessors = djikstra(graph, s_deb, s_fin)
    path = find_shortest_path(predecessors, s_deb, s_fin)
    w = -int(lines[0][0])
    for i, j in path:
        w += int(lines[i][j])

    lines = build_whole_grid(lines)
    graph = parse_graph(lines)
    s_deb = graph["S"][0]
    s_fin = graph["S"][-1]
    predecessors = djikstra(graph, s_deb, s_fin)
    path = find_shortest_path(predecessors, s_deb, s_fin)
    w2 = -int(lines[0][0])
    for i, j in path:
        w2 += int(lines[i][j])

    return w, w2


def parse_graph(lines):
    summits = []
    arcs = []
    for i, line in enumerate(lines):
        arc_line = []
        for j, w in enumerate(line):
            summits.append((i, j))
            arc_line.append(int(w))
        arcs.append(arc_line)
    return {
        "S": summits,
        "A": arcs,
    }


def djikstra(graph, s_deb, s_fin):
    p = set()
    summits = graph["S"]
    arcs = graph["A"]
    distances = {x: inf for x in summits}
    distances[s_deb] = 0
    predecessors = {}
    i_max = len(arcs)
    j_max = len(arcs[0])
    while len(p) < len(summits):
        a = find_next_summit(distances, p)
        p.add(a)
        for b, w in neighbors_not_in_p(arcs, a, p, i_max, j_max).items():
            if distances[b] > distances[a] + w:
                distances[b] = distances[a] + w
                predecessors[b] = a
        if s_fin == a:
            break
    return predecessors


def find_next_summit(distances, p):
    min = inf
    next = None
    for s, d in (x for x in distances.items() if x[0] not in p and x[1] != inf):
        if d < min:
            min = d
            next = s
    return next


def neighbors_not_in_p(arcs, a, p, i_max, j_max):
    neighbors = {}
    i, j = a
    if i > 0 and (i-1, j) not in p:
        neighbors[(i-1, j)] = arcs[i-1][j]
    if j > 0 and (i, j-1) not in p:
        neighbors[(i, j-1)] = arcs[i][j-1]
    if i < i_max - 1 and (i+1, j) not in p:
        neighbors[(i+1, j)] = arcs[i+1][j]
    if j < j_max - 1 and (i, j+1) not in p:
        neighbors[(i, j+1)] = arcs[i][j+1]
    return neighbors


def find_shortest_path(predecessors, s_deb, s_fin):
    path = []
    s = s_fin
    while s != s_deb:
        path.append(s)
        s = predecessors[s]
    path.append(s_deb)
    return reversed(path)


def build_whole_grid(lines):
    new_lines = []
    for line in lines:
        new_line = list(line)
        for i in range(4):
            new_line += list(shift(line, i+1))
        new_lines.append(new_line)
    new_grid = list(new_lines)
    for i in range(4):
        for line in new_lines:
            new_grid.append(list(shift(line, i+1)))
    return new_grid


def shift(line, i):
    for x in line:
        yield str(int(x)+i) if int(x)+i <= 9 else str(int(x)+i-9)
