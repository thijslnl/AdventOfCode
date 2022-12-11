#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
def parse_data(data):
    monkeys = {}
    active_monkey = None
    factor = 1
    for line in data:
        if 'Monkey' in line:
            monkeys[line[7:].rstrip(':')] = {'items':[], 'operation': None, 'test': [None, None, None], 'inspected': 0}
            active_monkey = line[7:].rstrip(':')
        elif 'Starting items:' in line:
            for i in line.split(':', 1)[1].split(','):
                monkeys[active_monkey]['items'].append(int(i.strip('')))
        elif 'Operation:' in line:
            monkeys[active_monkey]['operation'] = line.split(' = ')[-1]
        elif 'Test' in line:
            monkeys[active_monkey]['test'][0] = int(line.split(' ')[-1])
            factor *= int(line.split(' ')[-1])
        elif 'true' in line:
            monkeys[active_monkey]['test'][1] = line.split(' ')[-1]
        elif 'false' in line:
            monkeys[active_monkey]['test'][2] = line.split(' ')[-1]
    return (monkeys, factor)

def run_play(monkeys:dict, factor:int, rounds:int, correction:int) -> list:
    for i in range(rounds):
        for monkey, value in monkeys.items():
            items = value['items']
            monkeys[monkey]['items'] = []
            for item in items:
                monkeys[monkey]['inspected'] += 1
                right = value['operation'].split(' ')[-1]
                right = item if right == 'old' else int(right)
                if '*' in value['operation']:
                    temp_item = item * right
                elif '+' in value['operation']:
                    temp_item = item + right 
                temp_item = temp_item // correction
                temp_item = temp_item % factor
                if temp_item % value["test"][0] == 0:
                    target = value["test"][1]
                else:
                    target = value["test"][2]
                monkeys[target]['items'].append(temp_item)
    inspected = [value['inspected'] for value in monkeys.values()]
    inspected.sort()
    return inspected

#day calculation
def a(data):
    rounds = 20
    correction = 3
    monkeys, factor = parse_data(data)
    inspected = run_play(monkeys, factor, rounds, correction)
    return inspected[-2]*inspected[-1]

def b(data):
    rounds = 10000
    correction = 1
    monkeys, factor = parse_data(data)
    inspected = run_play(monkeys, factor, rounds, correction)
    return inspected[-2]*inspected[-1]

#run script
if __name__ == '__main__': 
    main(year=2022, day=11, exampleOutput={'A':10605, 'B':2713310158}, funcs={'a': a, 'b': b})