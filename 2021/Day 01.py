#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods

#day calculation
def a(data):
    data = [int(i) for i in data]
    check = [x < data[i+1] for i, x in enumerate(data[:-1])]
    return sum(check)

def b(data):
    data = [int(i) for i in data]
    sums = [sum(data[i:i+3]) for i in range(len(data[:-2]))]
    check = [x < sums[i+1] for i, x in enumerate(sums[:-1])]
    return sum(check)

#run script
if __name__ == '__main__': 
    main(year=2021, day=1, exampleOutput={'A':7, 'B':5}, funcs={'a': a, 'b': b})