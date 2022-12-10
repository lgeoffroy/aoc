from advent_of_code_ocr import convert_6


def lvl1(lines):
    x, cycle = 1, 0
    cycles, signals = [20, 60, 100, 140, 180, 220], []
    for line in lines:
        cycle += 1
        if cycle in cycles:
            signals.append(cycle * x)
        if line != "noop":
            cycle += 1
            if cycle in cycles:
                signals.append(cycle * x)
            x += int(line.split(" ")[1])
    return sum(signals)


def lvl2(lines):
    screen = [["?"] * 40 for _ in range(6)]
    x, is_adding, current_line = 1, False, None
    lines = iter(lines)
    for c in range(240):
        screen[c // 40][c % 40] = "#" if c % 40 in [x - 1, x, x + 1] else "."
        if is_adding:
            is_adding = False
            x += int(current_line.split(" ")[1])
        else:
            current_line = next(lines)
            is_adding = current_line.startswith("addx")
    try:
        return convert_6("\n".join(map(lambda x: "".join(x), screen)))
    except KeyError:
        print("Couldn't OCR the result")
        for line in screen:
            print("".join(line))


def solve(lines):
    return lvl1(lines), lvl2(lines)
