#!/usr/bin/python3.5

import datetime
from dotenv import load_dotenv
import os
import requests
import sys
import timeit

from day1 import solve as solve_day1
from day2 import solve as solve_day2
from day3 import solve as solve_day3
from day4 import solve as solve_day4
from day5 import solve as solve_day5
from day6 import solve as solve_day6
from day7 import solve as solve_day7
from day8 import solve as solve_day8
from day9 import solve as solve_day9
from day10 import solve as solve_day10
from day11 import solve as solve_day11
from day12 import solve as solve_day12
from day13 import solve as solve_day13
from day14 import solve as solve_day14
from day15 import solve as solve_day15


load_dotenv()
SESSION_COOKIE = os.getenv('SESSION_COOKIE')


def get_level_input(level):
    headers = {
        'Accept-Charset': 'UTF-8',
        'Cookie': 'session=' + SESSION_COOKIE,
    }
    return requests.get('https://adventofcode.com/2020/day/' + str(level) + '/input', headers=headers).text


def get_input(level):
    filename = 'input/day' + level + '.txt'
    if os.path.exists(filename):
        f = open(filename, 'r')
        input = f.read()
        f.close()
        return input
    input = get_level_input(level)
    f = open(filename, 'w')
    f.write(input)
    f.close()
    return input

if __name__ == '__main__':
    try:
        levels = sys.argv[1:]
    except:
        levels = []
    if len(levels) == 0 or not all([int(level) in range(1, 16) for level in levels]):
        print('Usage: ' + sys.argv[0] + ' LEVEL [OTHER_LEVEL]...')
        print('Example: ' + sys.argv[0] + ' 1 3 4')
        exit(1)
    for level in levels:
        lines = get_input(level).splitlines()
        def resolve():
            results = globals()['solve_day' + level](lines)
            print('Level ' + level + ': ', end='')
            print(results)
        t = timeit.Timer(lambda: resolve())
        ts = t.timeit(1)
        print('    Exec time: ' + str(round(ts * 1000, 3)) + 'ms')
