from utils import get_level_input

def get_id(seat):
    binary_seat = seat. \
        replace('F', '0'). \
        replace('B', '1'). \
        replace('R', '1'). \
        replace('L', '0')
    return int(binary_seat, 2)

input = get_level_input(5)

def solve1():
    highest = ('FFFFFLLL', 0)
    for seat in input.splitlines():
        id = get_id(seat)
        if (id > highest[1]):
            highest = (seat, id)
    return highest[1]

def solve2(max):
    all_seats = []
    for seat in input.splitlines():
        all_seats.append(get_id(seat))
    for i in range(1, max):
        if not i in all_seats and (i-1) in all_seats:
            return i

def solve():
    max = solve1()
    return (max, solve2(max))
