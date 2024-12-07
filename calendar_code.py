from Environment import Environment
import requests
def get_calendar_data(env:Environment, day=1, year=2024):
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",cookies={'session': env.session_id}, headers={'User-Agent': env.agent_id})
    return response.text

results = get_calendar_data(Environment())

def format_text(results:str)-> list[int]:
    output = []
    for item in results.splitlines():
        output.append(item.split())
    res1, res2 = map(list, zip(*output))
    res1 = list(map(int, res1))
    res2 = list(map(int, res2))
    return res1, res2 

left_list, right_list = format_text(results)


def solve(left_list:list[int], right_list:list[int]):
    left_list.sort()
    right_list.sort()
    total = 0
    for left, right in zip(left_list, right_list):
        total = total + abs(left - right) 
    return total

print(solve(left_list, right_list))

def solve_2(left_list:list[int], right_list:list[int]):
    counter_for_right = {}
    for item in right_list:
        if item in counter_for_right.keys():
            counter_for_right[item] += 1
        else:
            counter_for_right[item] = 1
    result = 0
    for item in left_list:
        result += item * counter_for_right.get(item, 0)
    return result
print(solve_2(left_list, right_list))
        


    
    
    
    