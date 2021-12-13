#import main methods
import os, sys

from numpy.core.defchararray import count
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
from collections import defaultdict
from collections import Counter

def make_connections(data):
    connections = defaultdict(list)
    for line in data:
        a, b = line.split('-')
        if a != 'start':
            connections[b].append(a)
        if b != 'start':
            connections[a].append(b)
    connections.pop('end')
    return connections

def follow_path_a(connections, node, end, path, paths):
    for new_node in [x for x in connections[node] if x not in path or x.upper() == x]:
        new_path = path[:]
        new_path.append(new_node)
        if new_node == end:
            paths.append(new_path)
        else:
            follow_path_a(connections, new_node, end, new_path, paths)
    return paths

def follow_path_b(connections, node, end, path, paths, small_caves):
    check_path = [x for x in path if x in small_caves]
    count_small_caves = Counter(check_path)
    if count_small_caves.most_common(1):
        check_small_caves = count_small_caves.most_common(1)[0][1]
    else:
        check_small_caves = 0
    #print(check_small_caves)
    for new_node in [x for x in connections[node] if check_small_caves < 2 or (check_small_caves == 2 and x not in path) or x.upper() == x]:
        new_path = path[:]
        new_path.append(new_node)
        if new_node == end:
            paths.append(new_path)
        else:
            follow_path_b(connections, new_node, end, new_path, paths, small_caves)
    return paths


#day calculation
def a(data):
    connections = make_connections(data)
    start = 'start'
    end = 'end'
    paths = follow_path_a(connections, start, end, [start], [])
    return len(paths)

def b(data):
    connections = make_connections(data)
    start = 'start'
    end = 'end'
    small_caves = [x for x in connections if x.lower() == x and x != start]
    paths = follow_path_b(connections, start, end, [start], [], small_caves)
    return len(paths)

#run script
if __name__ == '__main__': 
    main(year=2021, day=12, exampleOutput={'A':226, 'B':3509}, funcs={'a': a, 'b': b})