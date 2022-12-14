#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main
import json
import functools

#import day methods
def match_pairs(data:list) -> list:
    pairs = []
    for i in range(0, len(data), 3):
        pairs.append(data[i:i+2])
    return pairs

def handle_item(item):
    if isinstance(item, str):
        item = json.loads(item)
    if not isinstance(item, list):
        item = [item]
    return item

def compare_values(item1, item2) -> int:
    item1 = handle_item(item1)
    item2 = handle_item(item2)
    values = list(zip(item1, item2))
    item1_len = len(item1)
    item2_len = len(item2)
    for l, r in values:
        if isinstance(l, list) or isinstance(r, list):
            status = compare_values(l, r)
            if status != 0:
                return status
        else:
            if l == r:
                continue
            elif l < r:
                return 1
            else:
                return -1
    if item1_len < item2_len:
        return 1
    elif item1_len > item2_len:
        return -1
    return 0

#day calculation
def a(data):
    pairs:list = match_pairs(data)
    correct:list = []
    for i, pair in enumerate(pairs, start=1):
        res = compare_values(pair[0], pair[1])
        if res == 1:
            correct.append(i)
    return sum(correct)

def b(data):
    divider_packets = ['[[2]]', '[[6]]']
    for packet in divider_packets:
        data.append(packet)
    data = [x for x in data if x != '']
    data.sort(key=functools.cmp_to_key(compare_values), reverse=True)
    x = [data.index(x)+1 for x in divider_packets]
    return x[0]*x[1]

#run script
if __name__ == '__main__': 
    main(year=2022, day=13, exampleOutput={'A':13, 'B':140}, funcs={'a': a, 'b': b})