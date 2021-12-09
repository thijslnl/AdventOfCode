#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
from functools import reduce

#day calculation
def a(data):
    mod_y = len(data[0])
    mod_x = len(data)
    steps = [1,3]
    y = 0
    trees = 0
    for i in range(0, len(data)+1, steps[0]):
        if data[i % mod_x][y % mod_y] == "#" and i < len(data):
            trees += 1
        y += steps[1]
    return trees

def b(data):
    mod_y = len(data[0])
    mod_x = len(data)
    trees = []
    steps = [(1,1),(1,3),(1,5),(1,7),(2,1)]
    for step in steps:
        step_tree = 0
        y = 0
        for s, i in enumerate(range(0, len(data)+1, step[0])):
            if data[i % mod_x][(y % mod_y)] == "#" and i < len(data):
                step_tree += 1
            y += step[1]
        trees.append(step_tree)
    return reduce((lambda x, y: x * y), trees)

#run script
if __name__ == '__main__': 
    main(year=2020, day=3, exampleOutput={'A':None, 'B':None}, funcs={'a': a, 'b': b})