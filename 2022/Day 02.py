#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
def check_result_a(line):
    a, b = line.split(' ')
    play = {'X': 1, 'Y': 2, 'Z': 3}
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    win = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    if b == draw[a]:
        score = 3
    elif win[a] == b:
        score = 0
    else:
        score = 6
    return score + play[b]

def check_result_b(line):
    a, b = line.split(' ')
    result = {'X': [-1, 0], 'Y': [0, 3], 'Z': [1, 6]}
    play = {'A': ['A', 'B', 'C'], 'B': ['B', 'C', 'A'], 'C': ['C', 'A', 'B']}
    point = {'A': 1, 'B' : 2, 'C' : 3}
    return result[b][1] + point[play[a][result[b][0]]]

#day calculation
def a(data):
    score = 0
    for line in data:
        score += check_result_a(line)
    return score

def b(data):
    score = 0
    for line in data:
        score += check_result_b(line)
    return score

#run script
if __name__ == '__main__': 
    main(year=2022, day=2, exampleOutput={'A':15, 'B':None}, funcs={'a': a, 'b': b})