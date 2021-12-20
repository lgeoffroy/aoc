from functools import reduce
from itertools import permutations, product
import numpy as np


def solve(lines):
    mapping = parse_map(lines)
    return len(mapping["beacons"]), manhattan(mapping["scanners"])


def manhattan(scanners):
    maxi = 0
    for x in scanners:
        for y in [s for s in scanners if not np.array_equal(x, s)]:
            maxi = max(maxi, sum(abs(a - b) for a, b in zip(x, y)))
    return maxi


def parse_map(lines):
    whole_map = {}
    maps = []
    current_map = {"beacons": [], "integrated": False}
    for line in lines:
        if line == "":
            maps.append(current_map)
            current_map = {"beacons": [], "integrated": False}
        elif line.startswith("---"):
            current_map["scanner"] = np.array([0, 0, 0], dtype=int)
        else:
            [x, y, z] = [float(a) for a in line.split(",")]
            current_map["beacons"].append(np.array([x, y, z], dtype=int))
    maps.append(current_map)
    integrate(whole_map, current_map)
    while not all(list(map(lambda x: x["integrated"], maps))):
        for m in [x for x in maps if not x["integrated"]]:
            m["integrated"] = integrate(whole_map, m)
    return whole_map


def get_rotations():
    def build_rotations_matrices():
        for x, y, z in permutations([0, 1, 2]):
            for sx, sy, sz in product([-1, 1], repeat=3):
                rotation_matrix = np.zeros((3, 3))
                rotation_matrix[0, x] = sx
                rotation_matrix[1, y] = sy
                rotation_matrix[2, z] = sz
                if np.linalg.det(rotation_matrix) == 1:
                    yield rotation_matrix

    for R in build_rotations_matrices():
        yield lambda map: {
            "beacons": [R.dot(x.transpose()) for x in map["beacons"]],
            "scanner": R.dot(map["scanner"]),
        }


def find_translation(rotated, whole_map):
    matches = {}
    for x in rotated["beacons"]:
        for y in whole_map["beacons"]:
            offset = y - x
            key = tuple(offset)
            if key not in matches:
                matches[key] = 0
            matches[key] += 1
            if matches[key] == 12:
                def translation(mapping):
                    return {
                        "beacons": [z + offset for z in mapping["beacons"]],
                        "scanner": mapping["scanner"] + offset,
                    }
                return translation
    return None


def integrate(whole_map, map):
    if not whole_map:
        whole_map["beacons"] = map["beacons"]
        whole_map["scanners"] = [map["scanner"]]
        return True
    for rotation in get_rotations():
        rotated = rotation(map)
        translation = find_translation(rotated, whole_map)
        if not translation:
            continue
        transformed = translation(rotated)
        whole_map["scanners"].append(transformed["scanner"])
        whole_map["beacons"] += [b for b in transformed["beacons"] if reduce(lambda acc, x: acc and not np.array_equal(x, b), whole_map["beacons"], True)]
        return True
    return False
