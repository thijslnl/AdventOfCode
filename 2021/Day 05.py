#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import numpy as np
from collections import defaultdict

def handle_data(line):
    x = [None, None]
    y = [None, None]
    x[0],y[0],x[1],y[1] = [np.double(i) for i in line.replace(' -> ', ',').split(',')]
    return (x, y)

def a(data):
    field = defaultdict(int)
    for line in data:
        x, y = handle_data(line)
        if x[0] == x[1] or y[0] == y[1]:
            for xx in np.arange(np.min(x), np.max(x)+1):
                for yy in np.arange(np.min(y), np.max(y)+1):
                    field[f'{xx}_{yy}'] += 1
    return len([k for k,v in field.items() if v > 1])

def b(data):
    field = defaultdict(int)
    for line in data:
        x, y = handle_data(line)
        if x[0] == x[1] or y[0] == y[1]:
            #print(line, x, y)
            for xx in np.arange(np.min(x), np.max(x)+1):
                for yy in np.arange(np.min(y), np.max(y)+1):
                    field[f'{xx}_{yy}'] += 1
            #print(field)
        elif np.max(x)-np.min(x) == np.max(y)-np.min(y):
            step_x = np.double(1 if x[1] > x[0] else -1)
            step_y = np.double(1 if y[1] > y[0] else -1)
            for xx, yy in zip(np.arange(x[0], np.double(x[1]+step_x), step_x), np.arange(y[0], np.double(y[1]+step_y), step_y)):
                field[f'{xx}_{yy}'] += 1
    return len([k for k,v in field.items() if v > 1])

#run script
if __name__ == '__main__': 
    main(year=2021, day='5', exampleOutput={'A':5, 'B':12}, funcs={'a': a, 'b': b})