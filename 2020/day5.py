def get_id(seat):
    binary_seat = seat. \
        replace('F', '0'). \
        replace('B', '1'). \
        replace('R', '1'). \
        replace('L', '0')
    return int(binary_seat, 2)

def solve1(lines):
    highest = ('FFFFFLLL', 0)
    for seat in lines:
        id = get_id(seat)
        if (id > highest[1]):
            highest = (seat, id)
    return highest[1]

def solve2(lines, max):
    all_seats = []
    for seat in lines:
        all_seats.append(get_id(seat))
    for i in range(1, max):
        if not i in all_seats and (i-1) in all_seats:
            return i

def solve(lines):
    max = solve1(lines)
    return (max, solve2(lines, max))
