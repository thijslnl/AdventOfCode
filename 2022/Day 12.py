#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main
import string
import numpy as np
from collections import deque

#import day methods
letters = list('S' + string.ascii_lowercase + 'E')

def find_points(data:list) -> tuple:
    for l, line in enumerate(data):
        if 'S' in line:
            start = (l, line.index('S'))
        if 'E' in line:
            end = (l, line.index('E'))
    return (start, end)

def find_starts(data:list) -> list:
    starts = []
    for l, line in enumerate(data):
        if 'S' in line:
            starts.append((l, line.index('S')))
        if 'a' in line:
            starts.append((l, line.index('a')))
    return starts

def valid(data, curValue, x, y):
    if x < 0 or x >= len(data) or y < 0 or y >= len(data[x]):
        return False
    return data[x][y] in list(range(1, curValue+2))

def solve(data, start, end):
    delta_x = [-1, 1, 0, 0]
    delta_y = [0, 0, 1, -1]
    Q = deque([start])
    dist = {start: 0}
    while len(Q):
        curPoint = Q.popleft()
        curValue = data[curPoint[0]][curPoint[1]]
        curDist = dist[curPoint]
        if curPoint == end:
            return curDist
        for dx, dy in zip(delta_x, delta_y):
            nextPoint = (curPoint[0] + dx, curPoint[1] + dy)
            if not valid(data, curValue, nextPoint[0], nextPoint[1]) or nextPoint in dist.keys():
                continue
            dist[nextPoint] = curDist + 1
            Q.append(nextPoint)

#day calculation
def a(data):
    start, end = find_points(data)
    data = np.array([[letters.index(l) for l in x] for x in data])
    data[data == 0] = 1
    data[data == 27] = 26
    data = data.tolist()
    steps = solve(data, start, end)
    return steps

def b(data):
    _, end = find_points(data)
    starts = find_starts(data)
    data = np.array([[letters.index(l) for l in x] for x in data])
    data[data == 0] = 1
    data[data == 27] = 26
    dis = 10e6
    for start in starts:
        dis = min(solve(data, start, end), dis)
    return dis

#run script
if __name__ == '__main__': 
    main(year=2022, day=12, exampleOutput={'A':31, 'B':29}, funcs={'a': a, 'b': b})