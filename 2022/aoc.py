#!/usr/bin/env python3

from dotenv import load_dotenv
import os
import getopt
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


load_dotenv()
SESSION_COOKIE = os.getenv("SESSION_COOKIE")


def get_level_input(level):
    headers = {
        "Accept-Charset": "UTF-8",
        "Cookie": f"session={SESSION_COOKIE}",
    }
    return requests.get(
        f"https://adventofcode.com/2022/day/{str(level)}/input", headers=headers
    ).text


class NotAvailableException(Exception):
    pass


def get_input(level, test=False):
    filename = f"input/{'test' if test else 'day'}{level}.txt"
    if os.path.exists(filename):
        f = open(filename, "r")
        input = f.read()
        f.close()
        return input
    input = get_level_input(level)
    if "Please" in input:
        raise NotAvailableException
    f = open(filename, "w")
    f.write(input)
    f.close()
    return input


def help():
    print(f"Usage: {sys.argv[0]} [OPTIONS]")
    print("Options:")
    print("  -h, --help             Display this help.")
    print("  -t, --test             Use test data.")
    print("  -l, --levels=1,3       Run only specific level(s) (comma separated).")
    sys.exit()


def parse_args(argv):
    test = False
    levels = range(1, 26)
    try:
        opts, args = getopt.getopt(argv[1:], "htl:", ["help", "test", "levels="])
    except getopt.GetoptError:
        help()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
        elif opt in ("-t", "--test"):
            test = True
        elif opt in ("-l", "--levels"):
            levels = [int(x) for x in arg.split(",")]
    return (test, levels)


if __name__ == "__main__":
    test, levels = parse_args(sys.argv)
    for level in levels:
        try:
            lines = get_input(level, test).splitlines()

            def resolve():
                results = globals()[f"solve_day{level}"](lines)
                print(f"Level {level}: {results}")

            t = timeit.Timer(resolve)
            ts = t.timeit(1)
            print(f"    Exec time: {str(round(ts * 1000, 3))}ms")
        except NotAvailableException:
            print(f"* level {level} doesn't exist yet!")
            sys.exit(1)
        except KeyError:
            print(f"* level {level} not implemented.")
            sys.exit(1)
