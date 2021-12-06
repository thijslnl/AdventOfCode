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
import re

#day calculation
def a(data):
    excluded = ['ab','cd', 'pq', 'xy']
    vowels = 'aeiou'
    double_letter = r"([a-z])\1"
    nice = 0
    for string in data:
        excl = [e for e in excluded if e in string]
        only_vowels = [l for l in string if l in vowels]
        match = re.findall(double_letter, string)
        #print(len(only_vowels), len(match), excl)
        if not excl and len(only_vowels) >= 3 and len(match) >= 1:
            nice += 1
    return nice

def b(data):
    nice = 0
    for string in data:
        check = 0 
        for i in range(len(string)-1):
            if string[i:i+2] in string[i+2:]:
                check += 1
                break
        for i in range(len(string)-2):
            if string[i] == string[i+2]:
                check += 1
                break
        if check == 2:
            nice += 1
    return nice

#run script
if __name__ == '__main__': 
    main(year=2015, day=5, exampleOutput={'A':2, 'B':None}, funcs={'a': a, 'b': b})