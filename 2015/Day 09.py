#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
from collections import defaultdict
import itertools

day = dict()


def handle_data(line):
    line = line.split(' ')
    start, end, distance = line[0], line[2], int(line[4])
    day['distances'][start][end] = distance
    day['distances'][end][start]  = distance
    day['locations'].update([start, end])

#day calculation
def a(data):
    day['locations'] = set()
    day['distances'] = defaultdict(dict)
    min_distance = 10e10
    best_trip = None
    for line in data:
        handle_data(line)
    trips = list(itertools.permutations(day['locations']))
    for trip in trips:
        try:
            distance = sum([day['distances'][trip[i]][trip[i+1]] for i in range(len(trip[:-1]))])
            if distance < min_distance:
                min_distance = distance
                best_trip = trip
        except:
            pass
    print(best_trip, min_distance)
    return min_distance

def b(data):
    day['locations'] = set()
    day['distances'] = defaultdict(dict)
    max_distance = 0
    best_trip = None
    for line in data:
        handle_data(line)
    trips = list(itertools.permutations(day['locations']))
    for trip in trips:
        try:
            distance = sum([day['distances'][trip[i]][trip[i+1]] for i in range(len(trip[:-1]))])
            if distance > max_distance:
                max_distance = distance
                best_trip = trip
        except:
            pass
    print(best_trip, max_distance)
    return max_distance


#run script
if __name__ == '__main__': 
    main(year=2015, day=9, exampleOutput={'A':605, 'B':982}, funcs={'a': a, 'b': b})