#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
def parse_input(data:list) -> list:
    ret = []
    for line in data:
        words = line.split(' ')
        ret.append([int(word.rstrip(',')) for word in words[2::2]])
    return ret

#day calculation
def a(data):
    print(parse_input(data))
    return True

def b(data):
    return True

#run script
if __name__ == '__main__': 
    main(year=2015, day=15, exampleOutput={'A':62842880, 'B':None}, funcs={'a': a, 'b': b})