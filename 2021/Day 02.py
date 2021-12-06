#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods

#day calculation
def a(data):
    pos = [0,0]
    move = {'forward':[1,0], 'up':[0,-1], 'down': [0,1]}
    for line in data:
        direction, steps = line.split(' ')
        pos = [x*int(steps)+a for x,a in zip(move[direction], pos)]
    return pos[0]*pos[1]

def b(data):
    pos = [0,0,0]
    move = {'forward': [1,0,0], 'up': [0,0,-1], 'down': [0,0,1]}
    for line in data:
        move['forward'][1] = pos[2]
        direction, steps = line.split(' ')
        pos = [x*int(steps)+a for x,a in zip(move[direction], pos)]
    return pos[0]*pos[1]

#run script
if __name__ == '__main__': 
    main(year=2021, day=2, exampleOutput={'A':150, 'B':900}, funcs={'a': a, 'b': b})