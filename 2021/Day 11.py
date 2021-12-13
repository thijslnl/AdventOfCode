#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import numpy as np

#day calculation
def a(data):
    octo = np.array([[int(x) for x in line] for line in data])
    steps = 100
    flashings = 0
    for step in range(steps):
        octo += 1
        flashed = []
        flashing = np.where(octo > 9)
        flashing = [[x,y] for x,y in zip(flashing[0], flashing[1])]
        while flashing:
            for x,y in flashing:
                min_x = max(x-1, 0)
                max_x = min(x+2, len(octo))
                min_y = max(y-1, 0)
                max_y = min(y+2, len(octo[0]))
                flashed.append([x,y])
                octo[min_x:max_x, min_y:max_y] += 1
            flashing = np.where(octo > 9)
            flashing = [[x,y] for x,y in zip(flashing[0], flashing[1]) if [x,y] not in flashed]
        flashings += len(np.where(octo > 9)[0])
        octo[np.where(octo > 9)] = 0
    return flashings

def b(data):
    octo = np.array([[int(x) for x in line] for line in data])
    steps = 10000
    flashings = 0
    for step in range(steps):
        octo += 1
        flashed = []
        flashing = np.where(octo > 9)
        flashing = [[x,y] for x,y in zip(flashing[0], flashing[1])]
        while flashing:
            for x,y in flashing:
                min_x = max(x-1, 0)
                max_x = min(x+2, len(octo))
                min_y = max(y-1, 0)
                max_y = min(y+2, len(octo[0]))
                flashed.append([x,y])
                octo[min_x:max_x, min_y:max_y] += 1
            flashing = np.where(octo > 9)
            flashing = [[x,y] for x,y in zip(flashing[0], flashing[1]) if [x,y] not in flashed]
        flashings += len(np.where(octo > 9)[0])
        octo[np.where(octo > 9)] = 0
        if len(flashed) == len(octo)*len(octo[0]):
            return step+1

#run script
if __name__ == '__main__': 
    main(year=2021, day=11, exampleOutput={'A':1656, 'B':195}, funcs={'a': a, 'b': b})