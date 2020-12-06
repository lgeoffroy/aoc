from dotenv import load_dotenv
import requests
import os

load_dotenv()

SESSION_COOKIE = os.getenv('SESSION_COOKIE')

def get_level_input(level):
    headers = {
        'Accept-Charset': 'UTF-8',
        'Cookie': 'session=' + SESSION_COOKIE,
    }
    return requests.get('https://adventofcode.com/2020/day/' + str(level) + '/input', headers=headers).text
