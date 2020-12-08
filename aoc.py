#!/usr/bin/python3.5

from dotenv import load_dotenv
import os
import requests
import sys

from day1 import solve as solve_day1
from day2 import solve as solve_day2
from day3 import solve as solve_day3
from day4 import solve as solve_day4
from day5 import solve as solve_day5
from day6 import solve as solve_day6
from day7 import solve as solve_day7
from day8 import solve as solve_day8


load_dotenv()
SESSION_COOKIE = os.getenv('SESSION_COOKIE')


def get_level_input(level):
    headers = {
        'Accept-Charset': 'UTF-8',
        'Cookie': 'session=' + SESSION_COOKIE,
    }
    return requests.get('https://adventofcode.com/2020/day/' + str(level) + '/input', headers=headers).text


if __name__ == '__main__':
    try:
        levels = sys.argv[1:]
    except:
        levels = []
    if len(levels) == 0 or not all([level in '12345678' for level in levels]):
        print('Usage: ' + sys.argv[0] + ' LEVEL [OTHER_LEVEL]...')
        print('Example: ' + sys.argv[0] + ' 1 3 4')
        exit(1)
    for level in levels:
        input = get_level_input(level)
        buffer = input.splitlines()
        results = globals()['solve_day' + level](buffer)
        print('Level ' + level + ': ', end='')
        print(results)
