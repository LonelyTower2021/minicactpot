import json

def calculate_payout(value):
    with open('payout.json', 'r') as json_fp:
        payout = json.load(json_fp)
        return payout[f'{value}']

def get_payout(selection):
    return calculate_payout(sum(selection))

def possible_values(known):
    return set(range(1, 10)).difference(known)

def average_payout(row, known):
    unknowns = possible_values(known)
    num_cells = len(row)

    if num_cells > 3:
        raise ValueError("Row size must be less than or equal to 3")

    if num_cells == 3:
        total = get_payout(row)
        combos = 1
    elif num_cells == 2:
        total = one_hidden_cell(row, unknowns)
        combos = get_total_permutations(len(unknowns))
    elif num_cells == 1:
        total = two_hidden_cell(row, unknowns)
        combos = get_total_permutations(len(unknowns), 2)
    else:
        total = three_hidden_cell(unknowns)
        combos = get_total_permutations(len(unknowns), 3)

    return total / combos

def get_total_permutations(num_obj, num_choice=1):
    import math
    n = math.factorial(num_obj)
    n_r = math.factorial(num_obj - num_choice)
    return n / n_r

def one_hidden_cell(row, unknowns):
    total = 0.0

    for unknown in unknowns:
        if unknown not in row:
            row.add(unknown)
            total += get_payout(row)
            row.remove(unknown)
    
    return total

def two_hidden_cell(row, unknowns):
    total = 0.0

    for unknown in unknowns:
        if unknown not in row:
            row.add(unknown)
            total += one_hidden_cell(row, unknowns)
            row.remove(unknown)

    return total

def three_hidden_cell(unknowns):
    total = 0.0
    row = set()

    for unknown in unknowns:
        row.add(unknown)
        total += two_hidden_cell(row, unknowns)
        row.remove(unknown)

    return total
