import re
from utils import get_level_input

def data_valid(field, string):
    match = re.match('^.*' + field + ':(.*?)( |$)', string)
    val = match.groups()[0]
    if field == 'byr':
        return 1920 <= int(val) <= 2002
    if field == 'iyr':
        return 2010 <= int(val) <= 2020
    if field == 'eyr':
        return 2020 <= int(val) <= 2030
    if field == 'hgt':
        h_match = re.match('(\d+)(in|cm)', val)
        if h_match is not None:
            groups = h_match.groups()
            if (groups[1] == 'in'):
                return 19 <= int(groups[0]) <= 76
            if (groups[1] == 'cm'):
                return 150 <= int(groups[0]) <= 193
    if field == 'hcl':
        return re.search('^#[a-f\d]{6}$', val) is not None
    if field == 'ecl':
        return re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', val) is not None
    if field == 'pid':
        return re.search('^\d{9}$', val) is not None
    return False

def is_valid(strings, validate_data):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    result = {}
    string = ' '.join(strings)
    for field in fields:
        if re.search(field + ':', string) and (not validate_data or data_valid(field, string)):
            result[field] = result[field] + 1 if field in result else 1
    for key in fields:
        if not key in result or result[key] != 1:
            return 0
    return 1

def count_valids(input, validate_data):
    buffer = []
    lines = input.splitlines()
    lines.append('')
    nb_valid = 0
    for line in lines:
        if line == '':
            nb_valid += is_valid(buffer, validate_data)
            buffer = []
        else:
            buffer.append(line)
    return nb_valid

def solve():
    input = get_level_input(4)
    return (count_valids(input, validate_data=False),
            count_valids(input, validate_data=True))
