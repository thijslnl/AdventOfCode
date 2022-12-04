#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods

#day calculation
def a(data):
    return True

def b(data):
    return True

#run script
if __name__ == '__main__': 
    main(year=2022, day=1, exampleOutput={'A':None, 'B':None}, funcs={'a': a, 'b': b})