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
from hashlib import md5

#day calculation
def a(data):
    c = 0
    hash = ''
    while hash != '00000':
        c += 1
        hash = md5((data[0]+str(c)).encode()).hexdigest()[:5]
    return c

def b(data):
    c = 0
    hash = ''
    while hash != '000000':
        c += 1
        hash = md5((data[0]+str(c)).encode()).hexdigest()[:6]
    return c

#run script
if __name__ == '__main__': 
    main(year=2015, day=4, exampleOutput={'A':1048970, 'B': None}, funcs={'a': a, 'b': b})