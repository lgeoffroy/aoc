def detect_message(data, size):
    for i in range(len(data) - size):
        if len(set(data[i : i + size])) == size:
            return i + size


def solve(lines):
    line = lines[0]
    return detect_message(line, 4), detect_message(line, 14)
