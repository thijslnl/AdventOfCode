#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main
import numpy as np

#import day methods
steps = {'U':[0, 1], 'D':[0, -1], 'R': [1, 0], 'L': [-1, 0]}

def minmax(i:int) -> int:
    return min(1,max(-1, i))

def sim_steps(data:list, knots:list) -> int:
    pos = {knot:[np.array([0,0])] for knot in knots}
    for line in data:
        d, s = line.split(' ')
        for _ in range(int(s)):
            for k, knot in enumerate(knots):
                if knot == 'h':
                    coor = np.add(pos.get(knot)[-1], steps[d])
                else:
                    coor = pos.get(knot)[-1]
                    sub = np.subtract(pos.get(knots[k-1])[-1], coor)
                    if sum(abs(sub)) > 1:
                        if any(abs(x) > 1 for x in sub):
                            t_dif = [0 if not x else (x-int(x/abs(x))) for x in sub]
                        else:
                            t_dif = [minmax(sub[0]), minmax(sub[1])]
                        coor = np.subtract(pos.get(knots[k-1])[-1], t_dif)
                pos[knot].append(coor)
    pos_t = ['_'.join(str(x)) for x in pos.get(knots[-1])]
    return len(set(pos_t))

#day calculation
def a(data):
    return sim_steps(data, ['h', 't'])

def b(data):
    return sim_steps(data, ['h', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

#run script
if __name__ == '__main__': 
    main(year=2022, day=9, exampleOutput={'A':None, 'B': None}, funcs={'a': a, 'b': b})