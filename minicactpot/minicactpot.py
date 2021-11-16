import json

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
        for unknown in unknowns:
            total += calculate_payout(sum(row) + unknown)
            count += 1
    elif len(row) == 1:
        for unknown in unknowns:
            for another in unknowns:
                new_row = {unknown, another}.union(row)
                if len(new_row) == 3:
                    total += calculate_payout(sum(new_row))
                    count += 1

    return total / count
