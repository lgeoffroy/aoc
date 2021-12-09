import regex

def solve(input):
    (error_rate, validator, valids) = get_error_rate(input)
    return (error_rate, get_departure_product(input, validator, valids))

def get_error_rate(input):
    fields = [
        'departure location',
        'departure station',
        'departure platform',
        'departure track',
        'departure date',
        'departure time',
        'arrival location',
        'arrival station',
        'arrival platform',
        'arrival track',
        'class',
        'duration',
        'price',
        'route',
        'row',
        'seat',
        'train',
        'type',
        'wagon',
        'zone',
    ]
    validator = {}

    error_rate = 0
    header_read = False
    valids = []
    for line in input:
        for field in fields:
            match = regex.match('^' + field + ': (\d+)-(\d+) or (\d+)-(\d+)$', line)
            if match:
                validator[field] = [int(x) for x in match.groups()]
                break
        if regex.search(r'nearby', line):
            header_read = True
            continue
        if header_read:
            ticket_valid = True
            for val in [int(x) for x in line.split(',')]:
                valid = False
                for [min1, max1, min2, max2] in validator.values():
                    if (val >= min1 and val <= max1) or (val >= min2 and val <= max2):
                        valid = True
                if not valid:
                    ticket_valid = False
                    error_rate += val
            if ticket_valid:
                valids.append(line)

    return (error_rate, validator, valids)

def invalid(mapping):
    for l in mapping.values():
        if len(l) > 1:
            return True
    return False

def get_departure_product(input, validator, valids):
    mapping = get_mapping(input, validator, valids)
    next_line_is_ticket = False
    for line in input:
        if next_line_is_ticket:
            ticket = [int(x) for x in line.split(',')]
            product = 1
            for key, value in mapping.items():
                if regex.search(r'^departure', key):
                    product *= ticket[value[0]]
            return product
        if regex.search(r'your ticket', line):
            next_line_is_ticket = True

def get_mapping(input, validator, valids):
    keys = validator.keys()
    mapping = {}
    for key in keys:
        mapping[key] = list(range(0, len(keys)))
    while invalid(mapping):
        for valid in valids:
            for i, x in enumerate([int(x) for x in valid.split(',')]):
                for (key, [min1, max1, min2, max2]) in validator.items():
                    if i in mapping[key] and (x < min1 or x > max2 or (x < min2 and x > max1)):
                        mapping[key].remove(i)
        for k, l in mapping.items():
            if len(l) == 1:
                for key in mapping.keys():
                    if key != k and l[0] in mapping[key]:
                        mapping[key].remove(l[0])
    return mapping
