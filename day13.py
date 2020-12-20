def solve(input):
    start_time = int(input[0])
    buses = [int(x) if x != 'x' else 0 for x in input[1].split(',')]
    return (get_next_bus_time(start_time, buses), get_timestamp_contest(buses))

def get_next_bus_time(start_time, buses):
    x = start_time
    while x < 2*start_time:
        for bus in buses:
            if bus > 0 and x % bus == 0:
                return bus * (x - start_time)
        x += 1

def get_timestamp_contest(buses):
    (total, rests) = get_rests(buses)
    return total

def get_rests(buses):
    if len(buses) == 1:
        return (buses[0], [0])
    (total, rests) = get_rests(buses[:-1])
    if buses[-1] == 0:
        return (total, rests + [-1])
    k = 1
    while True:
        total = k
        for i, x in reversed(list(enumerate(buses[:-1]))):
            if x == 0:
                continue
            total *= x
            total += rests[i]
        if total % buses[-1] == (1-len(buses)) % buses[-1]:
            return (total, rests + [k])
        k += 1
