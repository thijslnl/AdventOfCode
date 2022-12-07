#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods

def run_dirs(data:list) -> dict:
    current_folder = []
    sizes = {'/': 0}
    for line in data:
        if line[:4] == '$ cd':
            if line[5:] != '..':
                current_folder.append(line[5:])
                sizes['_'.join(current_folder)] = 0
            else: 
                current_folder.pop()
        else:
            a, _ = line.split(' ', 1)
            if a.isnumeric():
                for i, _ in enumerate(current_folder, start=1):
                    sizes['_'.join(current_folder[:i])] += int(a)
    return sizes

#day calculation
def a(data):
    sizes = run_dirs(data)
    size = sum([x for x in sizes.values() if x <= 100000])
    return size

def b(data):
    space = 70000000
    required = 30000000
    sizes = run_dirs(data)
    used = sizes.get('/', None)
    size = min([x for x in sizes.values() if x > required-(space-used)])
    return size

#run script
if __name__ == '__main__': 
    main(year=2022, day=7, exampleOutput={'A':95437, 'B':24933642}, funcs={'a': a, 'b': b})