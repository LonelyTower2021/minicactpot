import json
from pdb import set_trace

def calculate_payout(value):
    with open('payout.json', 'r') as json_fp:
        payout = json.load(json_fp)
        return payout[f'{value}']

def get_payout(selection):
    return calculate_payout(sum(selection))

def odds(possible, hidden):
    if (hidden > 1):
        return 1 / (possible * (possible - 1) / 2)
    else:
        return 1 / possible

def possible(known):
    return set(range(1, 10)).difference(known)

def average_payout(row, known):
    unknowns = possible(known)
    total = 0.0
    count = 0
    if len(row) == 2:
        total, count = one_hidden_cell(row, unknowns)
    elif len(row) == 1:
        total, count = two_hidden_cell(row, unknowns)

    return total / count

def one_hidden_cell(row, unknowns):
    total = 0.0
    count = 0

    for unknown in unknowns:
        if unknown in row:
            continue
        else:
            row.add(unknown)
            total += calculate_payout(sum(row))
            row.remove(unknown)
    
    return total, count

def two_hidden_cell(row, unknowns):
    total = 0.0
    count = 0

    for first in unknowns:
        row.add(first)
        curr_total, curr_count = one_hidden_cell(row, unknowns)
        total += curr_total
        count += curr_count
        row.remove(first)

    return total, count
