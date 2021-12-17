#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import math

#day calculation
def a(data):
    _, target = data[0].split(': ')
    _, y = [b.split('=')[1].split('..') for b in target.split(', ')]
    y = [int(i) for i in y]
    max_y = max(y)
    min_y = min(y)
    
    steps = {int(i):int(1/2*i*(i+1)) for i in range(min_y, -min_y+1)}
    y_steps = set()
    for i in steps:
        min_i = steps[i]-max_y
        max_i = steps[i]-min_y
        if any(min_i <= v <= max_i for v in steps.values()):
            y_steps.add(i)
    return steps[max(y_steps)]

def b(data):
    _, target = data[0].split(': ')
    x, y = [b.split('=')[1].split('..') for b in target.split(', ')]
    x = [int(i) for i in x]
    y = [int(i) for i in y]
    max_y = max(y)
    min_y = min(y)
    max_x = max(x)
    min_x = min(x)

    steps = {int(i):int(1/2*i*(i+1)) for i in range(min_y, -min_y+1)}

    velo_min_x = math.floor((min_x*2)**(1/2))
    y_steps = set()
    for i in steps:
        min_i = steps[i]-max_y
        max_i = steps[i]-min_y
        if any(min_i <= v <= max_i for v in steps.values()):
            y_steps.add(i)
    x_steps = set()
    for i in range(velo_min_x, max_x+1):
        sum_x = 0
        for s in range(i,0,-1):
            sum_x += s
            if min_x <= sum_x <= max_x:
                x_steps.add(i)
                break
    possible_velos = []
    for vx in x_steps:
        for vy in y_steps:
            px, py = 0, 0
            temp_vx, temp_vy = vx, vy
            while px <= max_x and py >= min_y:
                px += temp_vx
                py += temp_vy
                temp_vx = max(temp_vx-1, 0)
                temp_vy -= 1
                if min_x <= px <= max_x and min_y <= py <= max_y:
                    possible_velos.append([vx, vy])
                    break
                if px > max_x or py < min_y:
                    break
    return len(possible_velos)

#run script
if __name__ == '__main__': 
    main(year=2021, day=17, exampleOutput={'A':45, 'B':112}, funcs={'a': a, 'b': b})