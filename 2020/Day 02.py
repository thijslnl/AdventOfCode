#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods

#day calculation
def a(data):
    c_p = 0
    for l in data:
        cont = l.split(" ")
        limits = cont[0].split("-")
        let = cont[1].rstrip(':')
        if int(limits[0]) <= cont[2].count(let) <= int(limits[1]):
            c_p +=1
    return c_p

def b(data):
    c_p = 0
    for l in data:
        cont = l.split(" ")
        limits = cont[0].split("-")
        let = cont[1].rstrip(':')
        if len(cont[2])>=int(limits[1]):
            if (cont[2][int(limits[0])-1] == let) ^ (cont[2][int(limits[1])-1] == let):
                c_p+=1
        else:
            if (cont[2][int(limits[0])-1] == let):
                c_p+=1
    return c_p

#run script
if __name__ == '__main__': 
    main(year=2020, day=2, exampleOutput={'A':None, 'B':None}, funcs={'a': a, 'b': b})