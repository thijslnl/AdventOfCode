#load main functions
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#set main variables
exampleResult = {}
exampleTime = {}
inputResult = {}
inputTime = {}
day = {'a': dict(), 'b': dict()}

#load day functions

#day calculation
def a(data):
    day['a']['feet'] = 0
    for item in data:
        d = [int(dim) for dim  in item.split('x')]
        d.sort()
        feet = 3*d[0]*d[1]+2*d[1]*d[2]+2*d[2]*d[0]
        day['a']['feet'] += feet
    return day['a']['feet']

def b(data):
    day['b']['ribbon'] = 0
    for item in data:
        d = [int(dim) for dim  in item.split('x')]
        d.sort()
        ribbon = 2*d[0]+2*d[1]+d[0]*d[1]*d[2]
        day['b']['ribbon'] += ribbon
    return day['b']['ribbon']

#run script
if __name__ == '__main__':
    main(year=2015, day=2, exampleOutput={'A':58, 'B':34}, funcs={'a': a, 'b': b})