#import main methods
import os, sys

from numpy.core.numeric import indices
from numpy.lib.utils import source
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import numpy as np

def create_paper(data):
    datapoints = {'x':[], 'y':[]}
    folds = []
    for line in data:
        if 'fold along' in line:
            folds.append(line.replace('fold along ', ''))
        elif line == '':
            continue
        else:
            x,y = line.split(',')
            datapoints['x'].append(int(x))
            datapoints['y'].append(int(y))
    paper = np.zeros((max(datapoints['y'])+1, max(datapoints['x'])+1))
    for x,y in zip(datapoints['x'], datapoints['y']):
        paper[y][x] = 1
    return (paper, folds)

def fold_paper(paper, fold):
    axes = {'y':0,'x':1}
    axis, index = fold.split('=')
    index = int(index)
    bottom_paper = np.take(paper, indices=range(0,index),axis=axes[axis])
    top_paper = np.zeros(bottom_paper.shape)
    source_data = np.where(np.take(paper, indices=range(index+1,paper.shape[axes[axis]]),axis=axes[axis]) > 0)
    for y,x in zip(source_data[0], source_data[1]):
        if y <= top_paper.shape[0] and x <= top_paper.shape[1]:
            top_paper[y][x] = 1
    reverse_top = np.flip(top_paper, axes[axis])
    return bottom_paper + reverse_top

#day calculation
def a(data):
    paper, folds = create_paper(data)
    flipped = fold_paper(paper, folds[0])
    return len(np.where(flipped > 0)[0])

def b(data):
    paper, folds = create_paper(data)
    for fold in folds:
        paper = fold_paper(paper, fold)
    paper = [''.join([' ' if x == 0 else '#' for x in list(r)]) for r in list(paper)]
    for line in paper:
        print(line)

#run script
if __name__ == '__main__': 
    main(year=2021, day=13, exampleOutput={'A':17, 'B':None}, funcs={'a': a, 'b': b})