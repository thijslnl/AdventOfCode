#load main functions
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#set main variables
exampleResult = {}
exampleTime = {}
inputResult = {}
inputTime = {}
day = {'a': dict(), 'b': dict()}

#load day functions
import numpy as np

def switch(func, lights, x, y):
    xx,xy = x.split(',')
    yx,yy = y.split(',')
    if func == 'turn_on':
        lights[int(xx):int(yx)+1,int(xy):int(yy)+1] = 1
    elif func == 'turn_off':
        lights[int(xx):int(yx)+1,int(xy):int(yy)+1] = 0
    elif func == 'toggle':
        lights[int(xx):int(yx)+1,int(xy):int(yy)+1] = 1-lights[int(xx):int(yx)+1,int(xy):int(yy)+1]
    return lights

def bright(func, lights, x, y):
    xx,xy = x.split(',')
    yx,yy = y.split(',')
    if func == 'turn_on':
        lights[int(xx):int(yx)+1,int(xy):int(yy)+1] += 1
    elif func == 'turn_off':
        lights[int(xx):int(yx)+1,int(xy):int(yy)+1] -= 1
        lights[lights<0] = 0
    elif func == 'toggle':
        lights[int(xx):int(yx)+1,int(xy):int(yy)+1] += 2
    return lights

#day calculation
def a(data):
    lights = np.zeros((1000,1000))
    for line in data:
        line = line.replace('turn ', 'turn_')
        func, x, _, y = line.split(' ')
        lights = switch(func, lights, x, y)
    return np.sum(lights)

def b(data):
    lights = np.zeros((1000,1000))
    for line in data:
        line = line.replace('turn ', 'turn_')
        func, x, _, y = line.split(' ')
        lights = bright(func, lights, x, y)
    return np.sum(lights)

#run script
if __name__ == '__main__': 
    main(year=2015, day=6, exampleOutput={'A':None, 'B':None}, funcs={'a': a, 'b': b})