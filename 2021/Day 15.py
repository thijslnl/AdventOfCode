#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

import heapq

def calc_distances(grid, start, goal):
    distances = {position: float('inf') for position in grid}
    distances[start] = 0

    ab = [(0, start)]
    while len(ab) > 0:
        pos_distance, current_pos = heapq.heappop(ab)
        if pos_distance > distances[current_pos]:
            continue

        for neighbor, weight in grid[current_pos].items():
            distance = pos_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(ab, (distance, neighbor))

    return distances[goal]

def field_to_grid(field):
    grid = {}
    for r in range(len(field)):
        for c in range(len(field[0])):
            grid_node = {}
            if r-1 >= 0:
                grid_node[f'{r-1}_{c}'] = field[r-1][c]
            if c-1 >= 0:
                grid_node[f'{r}_{c-1}'] = field[r][c-1]
            if r+1 < len(field):
                grid_node[f'{r+1}_{c}'] = field[r+1][c]
            if c+1 < len(field):
                grid_node[f'{r}_{c+1}'] = field[r][c+1]
            grid[f'{r}_{c}'] = grid_node
    return grid

def expand_field(field, n):
    field = [[c+e if c+e < 10 else (c+e)-(((c+e)//9)*9) for e in range(n) for c in r] for r in field]
    new_field = []
    for e in range(n):
        new_field += [[c+e if c+e < 10 else (c+e)-(((c+e)//9)*9) for c in r] for r in field]
    return new_field

#day calculation
def a(data):
    field = [[int(x) for x in line] for line in data]
    grid = field_to_grid(field)
    return calc_distances(grid, '0_0', f'{len(field)-1}_{len(field[0])-1}')

def b(data):
    field = [[int(x) for x in line] for line in data]
    field = expand_field(field, 5)
    grid = field_to_grid(field)
    return calc_distances(grid, '0_0', f'{len(field)-1}_{len(field[0])-1}')

#run script
if __name__ == '__main__': 
    main(year=2021, day=15, exampleOutput={'A':40, 'B':315}, funcs={'a': a, 'b': b})