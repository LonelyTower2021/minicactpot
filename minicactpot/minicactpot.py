import json

def calculate_payout(value):
    with open('payout.json', 'r') as json_fp:
        payout = json.load(json_fp)
        return payout[f'{value}']

def get_payout(selection):
    return calculate_payout(sum(selection))

def odds(pool):
    return 1 / len(pool)

def possible(selection):
    return set(range(10)).difference(selection)
