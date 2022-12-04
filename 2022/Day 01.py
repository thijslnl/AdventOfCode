#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods

#day calculation
def a(data):
    mcal = 0
    cal = 0
    for line in data:
        if line == '':
            if cal > mcal:
                mcal = cal
            cal = 0
        else:
            cal += int(line)
    return mcal

def b(data):
    mcals = [0, 0, 0]
    cal = 0
    for line in data:
        if line == '':
            if cal > min(mcals):
                mcals.remove(min(mcals))
                mcals.append(cal)
            cal = 0
        else:
            cal += int(line)
    return sum(mcals)
    
#run script
if __name__ == '__main__': 
    main(year=2022, day=1, exampleOutput={'A':None, 'B':None}, funcs={'a': a, 'b': b})