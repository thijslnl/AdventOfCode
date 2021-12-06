#load main functions
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#load day functions
from collections import defaultdict
from ctypes import c_uint16

day = {'a': dict(), 'b': dict()}

def handle_instruction(temp_day, instruction, i, verbose=False):
    #global day
    ins = instruction.split(' ')
    if temp_day.get(ins[-1], None) == None:
        if len(ins) == 3:
            if all(i.isdigit() for i in ins[0]):
                temp_day[ins[-1]] = int(ins[0])
            elif temp_day.get(ins[0], None):
                temp_day[ins[-1]] = temp_day.get(ins[0])
        else:
            orders = ['NOT', 'AND', 'OR', 'RSHIFT', 'LSHIFT']
            order = [x for x in ins if x in orders][0]
            ins = [x for x in ins if x not in orders]
            required = {'NOT':[0], 'RSHIFT':[0], 'LSHIFT':[0], 'AND':[0,1], 'OR':[0,1],}
            fields = [temp_day.get(ins[x], ins[x]) for x in required[order]]
            try:
                fields = [int(i) for i in fields]
            except:
                pass
            if all(isinstance(f, int) for f in fields):
                if order == 'NOT':
                    temp_day[ins[-1]] = c_uint16(~fields[0]).value
                elif order =='AND':
                    temp_day[ins[-1]] = c_uint16(fields[0] & fields[1]).value
                elif order =='OR':
                    temp_day[ins[-1]] = c_uint16(fields[0] | fields[1]).value
                elif order =='RSHIFT':    
                    temp_day[ins[-1]] = c_uint16(fields[0] >> int(ins[1])).value
                elif order =='LSHIFT':
                    temp_day[ins[-1]] = c_uint16(fields[0] << int(ins[1])).value
    return temp_day

#day calculation
def a(data):
    #global day
    day['a'] = defaultdict(int)
    while day['a'].get('a', None) == None:
        for i, instruction in enumerate(data):
            day['a'] = handle_instruction(day['a'], instruction, i)
    return day['a'].get('a')

def b(data):
    day['b'] = defaultdict(int)
    day['b']['b'] = a(data)
    while day['b'].get('a', None) == None:
        for i, instruction in enumerate(data):
            day['b'] = handle_instruction(day['b'], instruction, i)
    return day['b'].get('a')

#run script
if __name__ == '__main__': 
    main(year=2015, day=7, exampleOutput={'A':123, 'B':None}, funcs={'a': a, 'b': b})