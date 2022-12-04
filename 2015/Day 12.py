#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import json

def recursive_sum(line, score=0, ignore_red=False):
    if isinstance(line, int):
        score += line
    elif isinstance(line, list):
        for item in line:
            score = recursive_sum(item, score, ignore_red)
    elif isinstance(line, dict):
        if not(ignore_red and 'red' in line.values()):
            for v in line.values():
                score = recursive_sum(v, score, ignore_red)
    return score

#day calculation
def a(data):
    score = 0
    for line in data:
        line = json.loads(line)
        score += recursive_sum(line, score)
    return score

def b(data):
    score = 0
    for line in data:
        line = json.loads(line)
        score += recursive_sum(line, score, True)
    return score

#run script
if __name__ == '__main__':
    main(year=2015, day=12, exampleOutput={'A':6, 'B':4}, funcs={'a': a, 'b': b})