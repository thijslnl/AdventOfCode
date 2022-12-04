#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import string
chars = string.ascii_lowercase + string.ascii_uppercase

#day calculation
def a(data):
    score = 0
    for line in data:
        l, r = line[:len(line)//2], line[len(line)//2:]
        for e in l:
            if e in r:
                score += chars.index(e)+1
                break
    return score

def b(data):
    score = 0
    for group in [data[x*3:x*3+3] for x in range(len(data)//3)]:
        for l in group[0]:
            if l in group[1] and l in group[2]:
                score += chars.index(l)+1
                break
    return score

#run script
if __name__ == '__main__': 
    main(year=2022, day=3, exampleOutput={'A':157, 'B':70}, funcs={'a': a, 'b': b})