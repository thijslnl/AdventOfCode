#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods'
def split_input(data:list) -> tuple:
    start = []
    sit = None
    for i, line in enumerate(data):
        if sit == None:
            if line != '':
                
                start.append(line)
            elif line == '':
                sit = start_arrangement(start)
        else:
            break
    com = data[i:]
    return (sit, com)

def start_arrangement(data:list) -> list:
    sit = []
    for line in data[::-1]:
        for i, char in enumerate(line[1::4]):
            if char.isnumeric():
                sit.append([])
            elif char != ' ':
                sit[i].append(char)
    return sit

def prep_line(line:str) -> tuple:
    words = line.split(' ')
    return (int(words[1]), int(words[3]), int(words[5]))

def transfer(sit:list, line:str, dir:int) -> list:
    n, a, b = prep_line(line)
    for x in sit[a-1][-n:][::dir]:
        sit[b-1].append(x)
    sit[a-1] = sit[a-1][:-n]
    return sit

#day calculation
def a(data):
    sit, com = split_input(data)
    for line in com:
        sit = transfer(sit, line, -1)
    res = ''.join([x[-1] for x in sit])
    return res

def b(data):
    sit, com = split_input(data)
    for line in com:
        sit = transfer(sit, line, 1)
    res = ''.join([x[-1] for x in sit])
    return res

#run script
if __name__ == '__main__': 
    main(year=2022, day=5, exampleOutput={'A':'CMZ', 'B':'MCD'}, funcs={'a': a, 'b': b})