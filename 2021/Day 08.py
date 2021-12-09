#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
from collections import Counter

#day calculation
def a(data):
    check = [2, 3, 4, 7]
    output = int(0)
    for line in data:
        _, o = [[len(x) for x in s.split(' ')] for s in line.split(' | ')]
        occurance = Counter(o)
        output += sum([v for k,v in occurance.items() if k in check])
    return output

def b(data):
    output = int(0)
    for line in data:
        position = {i:'' for i in range(7)}
        value = {i:'' for i in range(10)}
        i = [{''.join(sorted(x)):len(x) for x in s.split(' ')} for s in line.split(' | ')][0]
        _, o = [[''.join(sorted(x)) for x in s.split(' ')] for s in line.split(' | ')]
        #determine value 1, 4, 7, 8
        for k, v in i.items():
            if v == 2:
                value[1] = k
            elif v == 3:
                value[7] = k
            elif v == 4:
                value[4] = k
            elif v == 7:
                value[8] = k
        #determine position 0
        position[0] = [k for k in value[7] if k not in value[1]][0]
        #determine value 0, 6 and 9 and position 2, 3 and 6
        zero_six_or_nine = [k for k,v in i.items() if v == 6]
        for val in zero_six_or_nine:
            check_string = value[4]+position[0]
            left_over = [k for k in val if k not in check_string]
            not_used = [k for k in check_string if k not in val]
            if not not_used:
                value[9] = val
                position[6] = left_over[0]
            elif not_used[0] in value[1]:
                value[6] = val
                position[2] = not_used[0]
            elif not_used[0] not in value[1]:
                value[0] = val
                position[3] = not_used[0]
        #determine position 4
        position[4] = [k for k in value[8] if k not in value[9]][0]
        #determine value 2, 3 and 5
        two_three_or_five = [k for k, v in i.items() if v == 5]
        for val in two_three_or_five:
            check_string = value[9]
            left_over = [k for k in val if k not in check_string]
            not_used = [k for k in check_string if k not in val]
            if left_over:
                value[2] = val
            elif not_used[0] in value[1]:
                value[5] = val
            elif not_used[0] not in value[1]:
                value[3] = val
        value = {v:k for k,v in value.items()}
        output += int(''.join([str(value[x]) for x in o]))
    return output

#run script
if __name__ == '__main__': 
    main(year=2021, day=8, exampleOutput={'A':26, 'B':61229}, funcs={'a': a, 'b': b})