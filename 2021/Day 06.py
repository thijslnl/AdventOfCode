#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
from collections import Counter
new_fish = 8
birth_fish = 6

def evolve_fish(fishes):
    fishes = {k-1:v for k,v in fishes.items()}
    new_fishes = fishes.pop(-1, 0)
    fishes[birth_fish] = fishes.get(birth_fish, 0) + new_fishes
    fishes[new_fish] = fishes.get(new_fish, 0) + new_fishes
    return fishes

#day calculation
def a(data):
    days = 80
    fishes = Counter([int(t) for t in data[0].split(',')])
    for _ in range(days):
        fishes = evolve_fish(fishes)
    return sum(fishes.values())

def b(data):
    days = 256
    fishes = Counter([int(t) for t in data[0].split(',')])
    for _ in range(days):
        fishes = evolve_fish(fishes)
    return sum(fishes.values())

#run script
if __name__ == '__main__': 
    main(year=2021, day=6, exampleOutput={'A':5934, 'B':26984457539}, funcs={'a': a, 'b': b})