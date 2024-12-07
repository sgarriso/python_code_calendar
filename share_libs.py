import requests
from Environment import Environment
def get_calendar_data(env:Environment, day=1, year=2024):
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",cookies={'session': env.session_id}, headers={'User-Agent': env.agent_id})
    return response.text

def format_text(results:str)-> list[int]:
    output = []
    for item in results.splitlines():
        output.append(item.split())
    res1, res2 = map(list, zip(*output))
    res1 = list(map(int, res1))
    res2 = list(map(int, res2))
    return res1, res2 