#!/usr/bin/python3.5

import sys
from day1 import solve as solve_day1
from day2 import solve as solve_day2
from day3 import solve as solve_day3
from day4 import solve as solve_day4
from day5 import solve as solve_day5
from day6 import solve as solve_day6

if __name__ == '__main__':
    try:
        levels = sys.argv[1:]
    except:
        levels = []
    if len(levels) == 0 or not all([level in '123456' for level in levels]):
        print('Usage: ' + sys.argv[0] + ' LEVEL [OTHER_LEVEL]...')
        print('Example: ' + sys.argv[0] + ' 1 3 4')
        exit(1)
    for level in levels:
        results = globals()['solve_day' + level]()
        print('Level ' + level + ': ', end='')
        print(results)
