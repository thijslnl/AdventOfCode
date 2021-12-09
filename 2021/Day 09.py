#import main methods
import os, sys

from numpy.core.defchararray import find, lower
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import numpy as np

def find_low_points(field):
    checks = [[-1,0],[1,0],[0,-1],[0,1]]
    lower_fields = {}
    for r, row in enumerate(field):
        for c, cell in enumerate(row):
            control = 1
            for check in checks:
                check_row = r+check[0]
                check_column = c+check[1]
                if check_row >= 0 and check_column >= 0 and check_row < len(field) and check_column < len(field[0]):
                    if cell >= field[check_row][check_column]:
                        control = 0
            if control == 1:
                lower_fields[r,c] = cell
    return lower_fields

#day calculation
def a(data):
    field = [[int(x) for x in line] for line in data]
    lower_fields = find_low_points(field)
    return sum([x+1 for x in lower_fields.values()])

def b(data):
    basins = []
    field = [[int(x) for x in line] for line in data]
    lower_fields = find_low_points(field)
    checks = [[-1,0],[1,0],[0,-1],[0,1]]
    for pos, val in lower_fields.items():
        basin = {pos:val}
        new_basin = {pos:val}
        while new_basin:
            check_locations = new_basin.copy()
            new_basin = {}
            for p, v in check_locations.items():
                for check in checks:
                    check_row = p[0]+check[0]
                    check_column = p[1]+check[1]
                    if check_row >= 0 and check_column >= 0 and check_row < len(field) and check_column < len(field[0]):
                        if field[check_row][check_column] > v and field[check_row][check_column] != 9:
                            new_basin[check_row, check_column] = field[check_row][check_column]
            basin.update(new_basin)
        basins.append(basin)
    basin_len = sorted([len(x) for x in basins])
    return basin_len[-1]*basin_len[-2]*basin_len[-3]

#run script
if __name__ == '__main__': 
    main(year=2021, day=9, exampleOutput={'A':15, 'B':1134}, funcs={'a': a, 'b': b})