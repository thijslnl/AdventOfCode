#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
from itertools import groupby

def look_and_say(string, n, t=1):
    groups = [''.join(g) for _, g in groupby(string)]
    new_string = ''.join([f'{len(group)}{group[0]}' for group in groups])
    if t < n:
        return look_and_say(new_string, n, t+1)
    else:
        return new_string

#day calculation
def a(data):
    i = 40
    for line in data:
        string = look_and_say(line, i)
    return len(string)

def b(data):
    i = 50
    for line in data:
        string = look_and_say(line, i)
    return len(string)

#run script
if __name__ == '__main__': 
    main(year=2015, day=10, exampleOutput={'A':None, 'B':None}, funcs={'a': a, 'b': b})