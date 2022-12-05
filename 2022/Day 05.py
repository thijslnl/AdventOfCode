#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods'
def split_input(data:list) -> tuple:
    start = []
    com = []
    sit = None
    for line in data:
        if sit == None:
            if line != '':
                start.append(line)
            elif line == '':
                sit = start_arrangement(start)
        else:
            com.append(line)
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

#day calculation
def a(data):
    sit, com = split_input(data)
    for line in com:
        n, a, b = prep_line(line)
        for _ in range(n):
            sit[b-1].append(sit[a-1].pop())
    res = ''.join([x[-1] for x in sit])
    return res

def b(data):
    sit, com = split_input(data)
    for line in com:
        n, a, b = prep_line(line)
        temp = []
        for _ in range(n):
            temp.append(sit[a-1].pop())
        for t in temp[::-1]:
            sit[b-1].append(t)
    res = ''.join([x[-1] for x in sit])
    return res

#run script
if __name__ == '__main__': 
    main(year=2022, day=5, exampleOutput={'A':'CMZ', 'B':'MCD'}, funcs={'a': a, 'b': b})