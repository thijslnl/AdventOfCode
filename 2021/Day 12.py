#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
from collections import defaultdict

def make_connections(data):
    connections = defaultdict(list)
    for line in data:
        a, b = line.split('-')
        connections[a].append(b)
        connections[b].append(a)
    return connections

def follow_path(connections, start, end, path):
    if start == end:
        return path
    else:
        path

#day calculation
def a(data):
    connections = make_connections(data)
    print(connections)
    start = 'start'
    end = 'end'
    paths = []

    nodes = connections[start]
    for node in nodes:
        paths.append(follow_path(connections, node, end, [start]))
    return paths


def b(data):
    return True

#run script
if __name__ == '__main__': 
    main(year=2021, day=12, exampleOutput={'A':10, 'B':None}, funcs={'a': a, 'b': b})