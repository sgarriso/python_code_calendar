from player import Player
from share_libs import get_calendar_data, format_text
from Environment import Environment
from state_machine import TextSeq
from word_search import WordSearch
def day_1():
    results = get_calendar_data(Environment())



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


def day_2():
    results = get_calendar_data(Environment(),2)
    def format_text(results:str)->list[int]:
        output = []
        for item in results.splitlines():
            output.append(list(map(int, item.split())))
        return output
        
    list_numbers = format_text(results)
    def check_numbers(numbers, counter_check=False):
        length = len(numbers)
        if length <= 1:
            return True
        pointer_2 = 1
        left = numbers[0]
        right = numbers[pointer_2]
        slide =  True if left <= right else False
        counter = 0
        for pointer_1 in range(length-1):
            left = numbers[pointer_1]
            right = numbers[pointer_2]
            if slide:
                if  left >= right or not(1 <= abs(left-right) <= 3):
                    counter = counter + 1
                    if not counter_check:
                        return False
                    
            else:
               if left <= right or  not(1 <= abs(left-right) <= 3):
                   counter = counter + 1
                   if not counter_check:
                       return False
            pointer_2 = pointer_2 + 1
        if counter_check: 
            return False if counter >=2 else True
        else:
            return True

            
                
            
             
    def solve_1(list_numbers:list[int], counter_check=False):
        results = []
        for numbers in list_numbers:
            results.append(check_numbers(numbers, counter_check))
        return sum(results)
    print(solve_1(list_numbers))
    print(solve_1(list_numbers, True))

def day3():
    data = get_calendar_data(Environment(),3)
    def solve1(data):
        InSeq = TextSeq()
        result = InSeq.feeder(list(data))
        total = 0
        for string in result:
            result = InSeq.feeder_2(list(string))
            total = total + (result[0] * result[1])
        return total
    print(solve1(data))
def day4():
    data = get_calendar_data(Environment(),4)
    mat = []
    for line in data.splitlines():
        mat.append(list(line))
    ws = WordSearch(mat, 'XMAS')
    print(ws.find_words())

def day6():
    data = get_calendar_data(Environment(), 6)
    dataset = []
    for i in data.splitlines():
        dataset.append(list(i))
    player = Player(dataset)
    player.moving(dataset)
    print(len(player.path.keys()))

day6()
        
        
    
    
    
        


    
    
    
    