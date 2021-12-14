#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
from collections import Counter

def get_rules(data):
    rules = {}
    for line in data:
        pair, insert = line.split(' -> ')
        rules[pair] = insert
    return rules

def develop_polymer(rules, polymer, steps, step):
    pairs = [polymer[i:i+2] for i in range(len(polymer)-1)]
    polymer = ''
    for i, pair in enumerate(pairs):
        polymer += pair[0]+rules.get(pair,'')
        if i+1 == len(pairs):
            polymer += pair[1]
    if step == steps:
        return polymer
    else:
        polymer = develop_polymer(rules, polymer, steps, step+1)
    return polymer

#day calculation
def a(data):
    day_data = data[:]
    polymer = day_data.pop(0)
    if day_data[0] == '':
        day_data.pop(0)
    rules = get_rules(day_data)
    polymer = develop_polymer(rules, polymer, 10, 1)
    polymer_count = Counter(polymer).most_common()
    return polymer_count[0][1]-polymer_count[-1][1]

def b(data):
    day_data = data[:]
    polymer = day_data.pop(0)
    if day_data[0] == '':
        day_data.pop(0)
    rules = get_rules(day_data)
    polymer = develop_polymer(rules, polymer, 40, 1)
    polymer_count = Counter(polymer).most_common()
    return polymer_count[0][1]-polymer_count[-1][1]

#run script
if __name__ == '__main__': 
    main(year=2021, day=14, exampleOutput={'A':1588, 'B':2188189693529}, funcs={'a': a, 'b': b})