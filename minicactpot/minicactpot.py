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
