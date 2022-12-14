#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main
import numpy as np

#import day methods
def build_field(field:np.ndarray, start:list, x:list, y:list, rocks:list) -> np.ndarray:
    field[start[1]-y[0], start[0]-x[0]] = 3
    for rock in rocks:
        for i in range(len(rock[:-1])):
            begin, end = rock[i], rock[i+1]
            c:list = [min(begin[1], end[1]), max(begin[1], end[1])]
            r:list = [min(begin[0], end[0]), max(begin[0], end[0])]
            field[c[0]-y[0]:c[1]-y[0]+1, r[0]-x[0]:r[1]-x[0]+1] = 2
    return field

def check_valid_pos(p:list, field:np.ndarray) -> bool:
    if p[0] < 0 or p[0] < 0 or p[1] > len(field[0]):
        return False
    return True

def throw_sand(field:np.ndarray, i:int, rel_start:list) -> int:
    sand_pos:list = rel_start
    prev_pos:list = [None, None]
    while sand_pos != prev_pos:
        prev_pos = sand_pos
        d = np.add(sand_pos, [1, 0])
        l = np.add(sand_pos, [1, -1])
        r = np.add(sand_pos, [1, -1])
        if check_valid_pos(d, field):
            if field[d] == 0:
                sand_pos = d
            elif field[l] == 0:
                sand_pos = l
            elif field[r] == 0:
                sand_pos = r
            return i
            field[] == 0:
            sand_pos = np.add(sand_pos, [1,0])
        elif field[np.add(sand_pos, [1,-1])] == 0:
            sand_pos = np.add(sand_pos, [1,-1])
        elif field[np.add(sand_pos, [1,1])] == 0:
            sand_pos = np.add(sand_pos, [1,1])
    if
    
    return i

#day calculation
def a(data):
    start:list = [500, 0]
    x:list = [500, 500]
    y:list = [0, 0]
    rocks:list = []
    for line in data:
        points:list = [[int(x) for x in points.split(',')] for points in line.split(' -> ')]
        rocks.append(points)
        for point in points:
            x:list = [min(point[0], x[0]), max(point[0], x[1])]
            y:list = [min(point[1], y[0]), max(point[1], y[1])]
    field = build_field(np.zeros([x[1]-x[0]+1, y[1]-y[0]+1]), start, x, y, rocks)
    n = throw_sand(field, 0, field[start[1]-y[0], start[0]-x[0]])
    return True

def b(data):
    return True

#run script
if __name__ == '__main__': 
    main(year=2022, day=14, exampleOutput={'A':24, 'B':None}, funcs={'a': a, 'b': b})