#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods

#day calculation
def a(data):
    contain = 0
    for line in data:
        a, b = line.split(',')
        a = [int(i) for i in a.split('-')]
        b = [int(i) for i in b.split('-')]
        a = range(a[0], a[1]+1)
        b = range(b[0], b[1]+1)
        if all(x in b for x in a) or all(x in a for x in b):
            contain += 1
    return contain

def b(data):
    overlap = 0
    for line in data:
        a, b = line.split(',')
        a = [int(i) for i in a.split('-')]
        b = [int(i) for i in b.split('-')]
        a = range(a[0], a[1]+1)
        b = range(b[0], b[1]+1)
        if any(x in b for x in a) or any(x in a for x in b):
            overlap += 1
    return overlap

#run script
if __name__ == '__main__': 
    main(year=2022, day=4, exampleOutput={'A':2, 'B':4}, funcs={'a': a, 'b': b})