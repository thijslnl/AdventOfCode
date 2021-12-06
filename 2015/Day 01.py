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
    day['a']['floor'] = 0
    for s in data[0]:
        if s == '(':
            day['a']['floor'] += 1
        elif s == ')':
            day['a']['floor'] -= 1
    return day['a']['floor']

def b(data):
    day['b']['floor'] = 0
    for i,s in enumerate(data[0]):
        if s == '(':
            day['b']['floor'] += 1
        elif s == ')':
            day['b']['floor'] -= 1
        if day['b']['floor'] == -1:
            return [i+1, day['b']['floor']]

if __name__ == '__main__':
    main(year=2015, day=1, exampleOutput={'A':None, 'B':None}, funcs={'a': a, 'b': b})