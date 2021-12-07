#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
from statistics import median

def moves_a(hpos, tpos):
    moves = [sum([int(abs(i-target)) for i in hpos]) for target in [tpos-1, tpos, tpos+1]]
    return moves

def moves_b(hpos, tpos):
    moves = [sum([int(abs(i-target)*(abs(i-target)+1)//2) for i in hpos]) for target in [tpos-1, tpos, tpos+1]]
    return moves

#day calculation
def a(data):
    hpos = [int(i) for i in data[0].split(',')]
    hpos = [int(i)-min(hpos) for i in hpos] if min(hpos) < 0 else hpos
    med = int(median(hpos))
    moves = moves_a(hpos, med)
    while moves[1] != min(moves):
        moves = moves_a(hpos, med+(moves.index(min(moves))-1))
    return moves[1]

def b(data):
    hpos = [int(i) for i in data[0].split(',')]
    hpos = [int(i)-min(hpos) for i in hpos] if min(hpos) < 0 else hpos
    mean = int(sum(hpos)//len(hpos))
    moves = moves_b(hpos, mean)
    while moves[1] != min(moves):
        moves = moves_b(hpos, mean+(moves.index(min(moves))-1))
    return moves[1]

#run script
if __name__ == '__main__': 
    main(year=2021, day=7, exampleOutput={'A':37, 'B':168}, funcs={'a': a, 'b': b})