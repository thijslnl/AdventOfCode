#import main methods
import os, sys

from numpy.lib.polynomial import poly
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main
from time import perf_counter

#import day methods asd
from collections import Counter
from collections import defaultdict

def get_rules(data):
    rules = {}
    for line in data:
        pair, insert = line.split(' -> ')
        rules[pair] = insert
    return rules

def dev_polymer(rules, polymers, letter_count, steps, step):
    new_polymers = defaultdict(int)
    for polymer, count in polymers.items():
        insert_letter = rules[polymer]
        new_pairs = [polymer[0]+insert_letter, insert_letter+polymer[1]]
        letter_count[insert_letter] += count
        for rule in new_pairs:
            new_polymers[rule] += count
    polymers = new_polymers
    if step < steps:
        polymers, letter_count = dev_polymer(rules, polymers, letter_count, steps, step+1)
    return (polymers, letter_count)

def run_day(data, steps):
    day_data = data[:]
    polymer = day_data.pop(0)
    letter_count = Counter(polymer)
    polymers = Counter([polymer[i:i+2] for i in range(len(polymer)-1)])
    if day_data[0] == '':
        day_data.pop(0)
    rules = get_rules(day_data)
    polymers, letter_count = dev_polymer(rules, polymers, letter_count, steps, 1)
    return letter_count.most_common()

#day calculation
def a(data):
    polymer_count = run_day(data, 10)
    return polymer_count[0][1]-polymer_count[-1][1]

def b(data):
    polymer_count = run_day(data, 40)
    return polymer_count[0][1]-polymer_count[-1][1]

#run script
if __name__ == '__main__': 
    main(year=2021, day=14, exampleOutput={'A':1588, 'B':2188189693529}, funcs={'a': a, 'b': b})