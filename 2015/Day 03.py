#load main functions
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#set main variables
exampleResult = {}
exampleTime = {}
inputResult = {}
inputTime = {}
day = {'a': dict(), 'b': dict()}

#load day functions
from collections import defaultdict

#day calculation
def a(data):
    x = 0
    y = 0
    houses = defaultdict(int)
    houses[f'{x}_{y}'] += 1
    for i, step in enumerate(data[0]):
        if step == '^':
            y += 1
        elif step == '>':
            x += 1
        elif step == 'v':
            y -= 1
        elif step == '<':
            x -= 1
        houses[f'{x}_{y}'] += 1
    return len(houses)

def b(data):
    x = 0
    y = 0
    rx = 0 
    ry = 0
    houses = defaultdict(int)
    houses[f'{x}_{y}'] += 2
    for i, step in enumerate(data[0]):
        r = i % 2
        if i%2 == 0:
            if step == '^':
                y += 1
            elif step == '>':
                x += 1
            elif step == 'v':
                y -= 1
            elif step == '<':
                x -= 1
            houses[f'{x}_{y}'] += 1
        else:
            if step == '^':
                ry += 1
            elif step == '>':
                rx += 1
            elif step == 'v':
                ry -= 1
            elif step == '<':
                rx -= 1
            houses[f'{rx}_{ry}'] += 1
    return len(houses)

#run script
if __name__ == '__main__': 
    main(year=2015, day=3, exampleOutput={'A':2, 'B':11}, funcs={'a': a, 'b': b})