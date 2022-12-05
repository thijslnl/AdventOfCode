#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
def parse_data(data) -> dict:
    reindeer = {}
    for line in data:
        words = line.split(' ')
        reindeer[words[0]] = [int(words[3]), int(words[6]), int(words[-2])]
    return reindeer
    
#day calculation
def a(data):
    sec = 2503
    distance = 0
    reindeer = parse_data(data)
    for deer in reindeer.values():
        n = sec//(deer[1]+deer[2])
        r = sec%(deer[1]+deer[2])
        dis = (n*deer[1]+min(r, deer[1]))*deer[0]
        distance = max(distance, dis)
    return distance

def b(data):
    sec = 2503
    reindeer = parse_data(data)
    scores = {deer:0 for deer in reindeer.keys()}
    distance = {deer:0 for deer in reindeer.keys()}
    for s in range(1, sec+1):
        for name, deer in reindeer.items():
            run = s%(deer[1]+deer[2])
            moving = 0 < run <= deer[1]
            distance[name] += deer[0] if moving else 0
        leaders = [name for name, dis in distance.items() if dis == max(distance.values())]
        for leader in leaders:
            scores[leader] += 1
    return max(scores.values())

#run script
if __name__ == '__main__': 
    main(year=2015, day=14, exampleOutput={'A':None, 'B':None}, funcs={'a': a, 'b': b})