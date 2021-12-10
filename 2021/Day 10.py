#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
def find_corrupted(line):
    openers = []
    for char in line:
        if char in pairs: 
            openers.append(char)
        elif openers == []:
            return char
        elif pairs[openers[-1]] == char:
            openers.pop(-1)
        else: 
            return char
    return None

pairs = {'(':')', '[':']', '{':'}', '<':'>'}

#day calculation
def a(data):
    syntax_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    found = [find_corrupted(line) for line in data]
    return sum([syntax_scores.get(x, 0) for x in found])

def b(data):
    autocomplete_scores = {')':1, ']': 2, '}': 3, '>': 4}
    cleaned_data = [line for line in data if not find_corrupted(line)]
    closed_all = []
    for line in cleaned_data:
        openers = []
        for char in line:
            if char in pairs: 
                openers.append(char)
            elif pairs[openers[-1]] == char:
                openers.pop(-1)
        closed = [autocomplete_scores[pairs[x]] for x in reversed(openers)]
        line_score = 0
        for score in closed:
            line_score = line_score*5+score
        closed_all.append(line_score)
    return sorted(closed_all)[len(closed_all)//2]

#run script
if __name__ == '__main__': 
    main(year=2021, day=10, exampleOutput={'A':26397, 'B':288957}, funcs={'a': a, 'b': b})