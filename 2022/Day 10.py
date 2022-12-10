#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
cycles:dict = {'noop': 1, 'addx': 2}

def run_cycle(n:int, cycle:int, X:int, checks:range, signal_strength:list) -> tuple:
    for _ in range(n):
        cycle += 1
        if cycle in checks:
            signal_strength.append(X*cycle)
    return (cycle, X, checks, signal_strength)

def draw_screen(n:int, cycle:int, X:int, screen:list) -> tuple:
    for _ in range(n):
        if (cycle-1)%40 in range(X-1, X+2):
            screen[cycle-1] = '#'
        cycle += 1
    return (cycle, X, screen)

#day calculation
def a(data):
    signal_strength:list = []
    X:int = 1
    cycle:int = 0
    checks:range = range(20, 221, 40)
    for line in data:
        command = line[:4]
        cycle, X, checks, signal_strength = run_cycle(cycles.get(command), cycle, X, checks, signal_strength)
        if command == 'addx':
            X += int(line[5:])
    return sum(signal_strength)

def b(data):
    X:int = 1
    cycle:int = 1
    screen:list = [*'.'*240]
    for line in data:
        command = line[:4]
        cycle, X, screen = draw_screen(cycles.get(command), cycle, X, screen)
        if command == 'addx':
            X += int(line[5:])
    for row in [screen[i:i+40] for i in range(0, len(screen), 40)]:
        print(''.join(row))
    return False

#run script
if __name__ == '__main__': 
    main(year=2022, day=10, exampleOutput={'A':13140, 'B':None}, funcs={'a': a, 'b': b})