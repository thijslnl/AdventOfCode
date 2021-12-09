#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods

#day calculation
def a(data):
    check = 2020
    data.sort()
    data = [int(x) for x in data]
    for l in data:
        if check-l in data:
            return l*(check-l)

def b(data):
    check = 2020
    data.sort()
    data = [int(x) for x in data]
    for l in data:
        for ll in [i for i in data if i > l]:
            if check-l-ll in data:
                return l*ll*(check-l-ll)
    return True

#run script
if __name__ == '__main__': 
    main(year=2020, day=1, exampleOutput={'A':None, 'B':None}, funcs={'a': a, 'b': b})