#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import re

#day calculation
def a(data):
    lit_count = 0
    char_count = 0
    for line in data:
        new_line = line.replace('\\"','_').replace('\\\\','_')
        groups = re.findall(r'(\\x..)', line)
        for group in groups:
            new_line = new_line.replace(group, '_')
        lit_count += len(line)
        char_count += len(new_line)-2
    print(lit_count, char_count)
    return lit_count - char_count

def b(data):
    lit_count = 0
    char_count = 0
    for line in data:
        new_line = line.replace('\\', '__').replace('"', '__')
        print(len(line), len(new_line)+2, line, new_line)
        lit_count += len(line)
        char_count += len(new_line)+2
    print(lit_count, char_count)
    return char_count - lit_count

#run script
if __name__ == '__main__': 
    main(year=2015, day=8, exampleOutput={'A':12, 'B':19}, funcs={'a': a, 'b': b})