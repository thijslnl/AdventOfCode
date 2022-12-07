#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
def check_start(line:str, n:int) -> int:
    for i, _ in enumerate(line[n:]):
        if len(set(line[i:i+n])) == n:
            return i+n

#day calculation
def a(data):
    score = 0
    for line in data:
        score += check_start(line, 4)
    return score

def b(data):
    score = 0
    for line in data:
        score += check_start(line, 14)
    return score

#run script
if __name__ == '__main__': 
    main(year=2022, day=6, exampleOutput={'A':39, 'B':120}, funcs={'a': a, 'b': b})