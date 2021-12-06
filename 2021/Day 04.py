#import main methods
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from aoc_helper import main
from time import perf_counter

#import day methods
import numpy as np

def handle_cards(work_data):
    cards = []
    columns = []
    card = -1
    for line in work_data:
        line = line.replace('  ', ' ')
        if line:
            cards[card].append([float(x) for x in line.split(' ') if x])
        else:
            cards.append([])
            card += 1
    for card in cards:
        numpy_array = np.array(card)
        transpose = numpy_array.T
        columns.append(transpose.tolist())
    return (np.array(cards), np.array(columns))


#day calculation
def a(data):
    work_data = data.copy()
    bingo_numbers = work_data.pop(0)
    cards, columns = handle_cards(work_data)
    for bingo_number in bingo_numbers.split(','):
        cards[np.where(cards == float(bingo_number))] = np.NaN
        columns[np.where(columns == float(bingo_number))] = np.NaN
        for card in cards:
            check = [np.isnan(x).all() for x in card]
            if any(check):
                return int(np.nansum(card) * float(bingo_number))
        for card in columns:
            check = [np.isnan(x).all() for x in card]
            if any(check):
                return int(np.nansum(card) * float(bingo_number))

def b(data):
    work_data = data.copy()
    bingo_numbers = work_data.pop(0)
    cards, columns = handle_cards(work_data)
    finished = list(range(len(cards)))
    for bingo_number in bingo_numbers.split(','):
        cards[np.where(cards == float(bingo_number))] = np.NaN
        columns[np.where(columns == float(bingo_number))] = np.NaN
        for c, card in enumerate(cards):
            if c in finished:
                check = [np.isnan(x).all() for x in card]
                if any(check):
                    if len(finished) > 1:
                        finished = [x for x in finished if x != c]
                    else:
                        return int(np.nansum(card) * float(bingo_number))
        for c, card in enumerate(columns):
            if c in finished:
                check = [np.isnan(x).all() for x in card]
                if any(check):
                    if len(finished) > 1:
                        finished = [x for x in finished if x != c]
                    else:
                        return int(np.nansum(card) * float(bingo_number))

#run script
if __name__ == '__main__': 
    main(year=2021, day='4_test', exampleOutput={'A':None, 'B':None}, funcs={'a': a, 'b': b})