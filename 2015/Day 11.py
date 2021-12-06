#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main

#import day methods
import string
import re
letters = list(string.ascii_lowercase)

def increment_password(password):
    password_index = [letters.index(x) for x in password]
    password_index[-1] += 1
    for i in range(len(password_index)-1,0, -1):
        if password_index[i] > 25:
            password_index[i-1] += 1
        password_index[i] = password_index[i] % 26
    password = ''.join([letters[x] for x in password_index])
    return (password, password_index)

#day calculation
def a(data):
    password = data[0]
    checks = [0,0,0]
    not_contain = ['i', 'o', 'l']
    while any(elem == 0 for elem in checks):
        checks = [0,0,0]
        password, password_index = increment_password(password)
        groups = re.findall(r'([a-z])\1{1}', password)
        if len(groups) >= 2:
            checks[0] = 1
        cant_contain = [x for x in not_contain if x in password]
        if len(cant_contain) == 0:
            checks[1] = 1
        consecutive = [x == (password_index[i+1] - 1) == (password_index[i+2] - 2) for i,x  in enumerate(password_index[:-2])]
        if any(x is True for x in consecutive):
            checks[2] = 1
    return password

def b(data):
    password = a(data)
    checks = [0,0,0]
    not_contain = ['i', 'o', 'l']
    while any(elem == 0 for elem in checks):
        checks = [0,0,0]
        password, password_index = increment_password(password)
        groups = re.findall(r'([a-z])\1{1}', password)
        if len(groups) >= 2:
            checks[0] = 1
        cant_contain = [x for x in not_contain if x in password]
        if len(cant_contain) == 0:
            checks[1] = 1
        consecutive = [x == (password_index[i+1] - 1) == (password_index[i+2] - 2) for i,x  in enumerate(password_index[:-2])]
        if any(x is True for x in consecutive):
            checks[2] = 1
    return password

#run script
if __name__ == '__main__': 
    main(year=2015, day=11, exampleOutput={'A':None, 'B':None}, funcs={'a': a, 'b': b})