#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods

#day calculation
def a(data):
    gamma = ''
    epsilon = ''
    for i, _ in enumerate(data[0]):
        vals = [x[i] for x in data]
        #g = int(vals.count('1')/len(vals) >= 0.5)
        g = int(vals.count('1') >= len(vals)*0.5)
        gamma+=str(g)
        epsilon+=str(1-g)
    return int(gamma,2)*int(epsilon,2)

def b(data):
    input_lists = {'o': data, 'c':data}
    for k,v in input_lists.items():
        for i, _ in enumerate(v[0]):
            vals = [x[i] for x in v]
            val_filter = int(vals.count('1') >= len(vals)*0.5)
            if k == 'c':
                val_filter = 1 - val_filter
            v = [x for x in v if x[i] == str(val_filter)]
            if len(v) == 1:
                break
        if k == 'o':
            oxygen = v[0]
        else:
            co2 = v[0]
    return int(oxygen,2)*int(co2,2)

#run script
if __name__ == '__main__': 
    main(year=2021, day=3, exampleOutput={'A':198, 'B':230}, funcs={'a': a, 'b': b})