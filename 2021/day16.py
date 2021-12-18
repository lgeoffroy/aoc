import math
from functools import reduce

def solve(input):
    bin_input = to_bin(input[0])
    parsed = parse_packet(bin_input, 1)[0]

    return level1(parsed), compute(parsed[0])


def level1(parsed):
    return reduce(lambda acc, x: acc + ((x["version"] + level1(x["value"])) if type(x["value"]) == list else x["version"]), parsed, 0)


def to_bin(packet):
    binary = bin(int(packet, 16))[2:]
    return binary.zfill(4*len(packet))


def parse_packet(packet, l):
    data = []
    x = 0
    while True:
        version = int(packet[x:x+3], 2)
        packet_type = int(packet[x+3:x+6], 2)
        if packet_type == 4:
            metadata = parse_data_packet(packet[x:])
            data.append(metadata)
            x += metadata["size"]
        else:
            length_type = "bits" if packet[x+6] == "0" else "packets"
            if length_type == "bits":
                length = int(packet[x+7:x+22], 2)
                size = 22 + length
                parsed = parse_packet(packet[x+22:x+22+length], math.inf)
                data.append({
                    "packet": packet[x:x+size],
                    "version": version,
                    "type": packet_type,
                    "value": parsed[0],
                    "size": size,
                    "length_type": length_type,
                    "length": length,
                })
            else:
                length = int(packet[x+7:x+18], 2)
                subpackets, size = parse_packet(packet[x+18:], length)
                size += 18
                data.append({
                    "packet": packet[x:x+size],
                    "version": version,
                    "type": packet_type,
                    "value": subpackets,
                    "size": size,
                    "length_type": length_type,
                    "length": length,
                })
            x += size
        if x == len(packet) or l == len(data):
            break
    return data, x


def parse_data_packet(packet):
    version = int(packet[0:3], 2)
    packet_type = int(packet[3:6], 2)
    value = 0
    i = 6
    while True:
        is_last = packet[i] == "0"
        value = value << 4 | int(packet[i+1:i+5], 2)
        i += 5
        if is_last:
            break
    return {
        "packet": packet[:i],
        "version": version,
        "type": packet_type,
        "value": value,
        "size": i,
    }


def product(lst):
    return 1 if len(lst) == 0 else lst[0] * product(lst[1:])


def greater(lst):
    return 1 if lst[0] > lst[1] else 0


def less(lst):
    return 1 if lst[0] < lst[1] else 0


def equal(lst):
    return 1 if lst[0] == lst[1] else 0


def compute(packet):
    if type(packet) == int:
        return packet
    map_operations = {
        0: lambda x: sum(list(map(compute, x["value"]))),
        1: lambda x: product(list(map(compute, x["value"]))),
        2: lambda x: min(list(map(compute, x["value"]))),
        3: lambda x: max(list(map(compute, x["value"]))),
        4: lambda x: compute(x["value"]),
        5: lambda x: greater(list(map(compute, x["value"]))),
        6: lambda x: less(list(map(compute, x["value"]))),
        7: lambda x: equal(list(map(compute, x["value"]))),
    }
    return map_operations[packet["type"]](packet)
