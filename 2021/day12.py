import re


def solve(lines):
    graph = get_graph(lines)
    little_rooms = [x for x in graph if x.lower() == x and x not in ["start", "end"]]

    memo = {}
    for node in little_rooms:
        memo[node] = find_paths(graph, node, [node], [], memo)

    paths_lvl1 = find_paths(graph, "start", ["start"], [], memo)
    lvl1 = len(paths_lvl1)

    cycles = {}
    for node in little_rooms:
        cycles[node] = find_paths(graph, node, [node], [], end=node)

    paths_lvl2 = []
    for path in paths_lvl1:
        paths_lvl2.append(path)
        for node in path:
            if node in cycles:
                paths_with_cycles = add_cycles(path, node, cycles[node])
                paths_lvl2.extend(x for x in paths_with_cycles if x not in paths_lvl2)
    lvl2 = len(paths_lvl2)

    return lvl1, lvl2


def add_cycles(path, node, cycles):
    paths = []
    useful_cycles = [
        cycle
        for cycle in cycles
        if not(any(map(lambda x: x.lower() == x and x != node and path.count(x) > 0, cycle)))
    ]
    for i, x in enumerate(path):
        if x == node:
            for cycle in useful_cycles:
                paths.append(path[:i] + cycle + path[i+1:])
    return paths


def get_graph(lines):
    nodes = {}
    for line in lines:
        match = re.match(r'^(\w+)-(\w+)$', line)
        first, second = match.groups()
        if first not in nodes:
            nodes[first] = [second]
        else:
            nodes[first].append(second)
        if second not in nodes:
            nodes[second] = [first]
        else:
            nodes[second].append(first)
    return nodes


def find_paths(graph, origin="start", visited=["start"], paths=[], memo={}, end="end"):
    next_nodes = graph[origin]
    for node in next_nodes:
        current_visited = list(visited)
        if node == end:
            current_visited.append(end)
            paths.append(current_visited)
        else:
            if node in ["start", "end"] or visited.count(node) == (2 if node == end else 1) and node.lower() == node:
                continue
            else:
                if node in memo:
                    new_paths = [
                        current_visited + x
                        for x in filter(
                            lambda subpath: not(any(map(
                                lambda y: y.lower() == y and y in current_visited,
                                subpath
                            ))),
                            memo[node],
                        )
                    ]
                else:
                    current_visited.append(node)
                    new_paths = find_paths(graph, origin=node, visited=current_visited, paths=paths, memo=memo, end=end)
                paths.extend(x for x in new_paths if x not in paths)
    return paths
