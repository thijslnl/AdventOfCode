#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import numpy as np

def handle_data(line):
    x = [None, None]
    y = [None, None]
    x[0],y[0],x[1],y[1] = [int(i) for i in line.replace(' -> ', ',').split(',')]
    return (x, y)
    
def determine_size(data):
    size = 0
    for line in data:
        x, y = handle_data(line)
        size = max([*x, *y, size])
    return [size+1, size+1]

def find_lines(field, x, y):
    if x[0] == x[1] or y[0] == y[1]:
        field[min(y):max(y)+1,min(x):max(x)+1] += 1
    return field

def a(data):
    size = determine_size(data)
    field = np.zeros(size)
    for line in data:
        x, y = handle_data(line)
        field = find_lines(field, x, y)
    return len(np.where(field > 1)[0])

def b(data):
    size = determine_size(data)
    field = np.zeros(size)
    for line in data:
        x, y = handle_data(line)
        field = find_lines(field, x, y)
        if max(x)-min(x) == max(y)-min(y):
            step_x = 1 if x[1] > x[0] else -1
            step_y = 1 if y[1] > y[0] else -1
            for xx, yy in zip(range(x[0], x[1]+step_x, step_x), range(y[0], y[1]+step_y, step_y)):
                field[yy, xx] += 1
    return len(np.where(field > 1)[0])

#run script
if __name__ == '__main__': 
    main(year=2021, day=5, exampleOutput={'A':5, 'B':12}, funcs={'a': a, 'b': b})