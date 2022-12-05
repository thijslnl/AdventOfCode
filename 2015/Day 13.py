#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main
import itertools

#import day methods
def create_options(data) -> dict:
    happiness = {}
    for line in data:
        words = line.split(' ')
        self, dir, amount, other = words[0], words[2], int(words[3]), words[-1].rstrip('.')
        amount = -1*amount if dir == 'lose' else amount
        if self not in happiness:
            happiness[self] = {other: amount}
        else:
            happiness[self][other] = amount
    return happiness

def seat_people(happiness, seat_options) -> int:
    scores = 0
    for seat_option in seat_options:
        score = 0
        seat_option = list(seat_option)
        n = len(seat_option)
        for i in range(n):            
            score += happiness.get(seat_option[i], {'me':0}).get(seat_option[(i-1)%n], 0)+happiness.get(seat_option[i], {'me':0}).get(seat_option[(i+1)%n], 0)
        scores = max(score, scores)
    return scores

#day calculation
def a(data):
    happiness = create_options(data)
    seat_options = list(itertools.permutations(happiness))
    scores = seat_people(happiness, seat_options)
    return scores

def b(data):
    happiness = create_options(data)
    names = list(happiness.keys())
    names.append('me')
    seat_options = list(itertools.permutations(names))
    scores = seat_people(happiness, seat_options)
    return scores

#run script
if __name__ == '__main__': 
    main(year=2015, day=13, exampleOutput={'A':330, 'B':None}, funcs={'a': a, 'b': b})