#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main
import numpy as np

#import day methods

#day calculation
def a(data):
    data = [[x for x in line] for line in data]
    npa = np.array(data, dtype=np.int32)
    score = 0
    for rn, r in enumerate(npa):
        for cn, c in enumerate(r):
            if cn == 0 or cn == len(r)-1 or rn == 0 or rn == len(npa)-1:
                score += 1
            elif all(c > i for i in npa[:rn, cn]) or all(c > i for i in npa[rn+1:, cn]) or all(c > i for i in npa[rn, :cn]) or all(c > i for i in npa[rn, cn+1:]):
                score += 1
    return score

def b(data):
    data = [[x for x in line] for line in data]
    npa = np.array(data, dtype=np.int32)
    dis = 0
    for rn, r in enumerate(npa):
        for cn, c in enumerate(r):
            if cn == 0 or cn == len(r)-1 or rn == 0 or rn == len(npa)-1:
                continue
            else:
                dirs = [npa[:rn, cn][::-1], npa[rn+1:, cn], npa[rn, :cn][::-1], npa[rn, cn+1:]]
                score = []
                for dir in dirs:
                    trees = 0
                    for i in dir:
                        trees += 1
                        if c <= i:
                            break
                    score.append(trees)
                dis = max(dis, np.product(score))        
    return dis

#run script
if __name__ == '__main__': 
    main(year=2022, day=8, exampleOutput={'A':21, 'B':8}, funcs={'a': a, 'b': b})