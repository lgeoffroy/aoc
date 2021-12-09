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
from day16 import solve as solve_day16
from day17 import solve as solve_day17
from day18 import solve as solve_day18
from day19 import solve as solve_day19
from day20 import solve as solve_day20
from day21 import solve as solve_day21
from day22 import solve as solve_day22
from day23 import solve as solve_day23
from day24 import solve as solve_day24
from day25 import solve as solve_day25


load_dotenv()
SESSION_COOKIE = os.getenv("SESSION_COOKIE")


def get_level_input(level):
    headers = {
        "Accept-Charset": "UTF-8",
        "Cookie": f"session={SESSION_COOKIE}",
    }
    return requests.get(f"https://adventofcode.com/2021/day/{str(level)}/input", headers=headers).text


def get_input(level):
    filename = f"input/day{level}.txt"
    if os.path.exists(filename):
        f = open(filename, "r")
        input = f.read()
        f.close()
        return input
    input = get_level_input(level)
    if "Please" in input:
        # day input does not exist yet
        return ''
    f = open(filename, "w")
    f.write(input)
    f.close()
    return input


if __name__ == "__main__":
    levels = sys.argv[1:]
    if not levels:
        levels = range(1, 26)
    if "-h" in levels or "--help" in levels or not all([int(level) in range(1, 26) for level in levels]):
        print(f"Usage: {sys.argv[0]} [LEVEL] [OTHER_LEVEL]...")
        print("Example:")
        print("  Run levels 1, 3 and 4: {sys.argv[0]} 1 3 4")
        print("  Run all levels: {sys.argv[0]}")
        exit(1)
    for level in levels:
        try:
            lines = get_input(level).splitlines()
            def resolve():
                results = globals()[f"solve_day{level}"](lines)
                print(f"Level {level}: ", end="")
                print(results)
            t = timeit.Timer(resolve)
            ts = t.timeit(1)
            print(f"    Exec time: {str(round(ts * 1000, 3))}ms")
        except NotImplementedError:
            print(f"* level {level} not implemented")
