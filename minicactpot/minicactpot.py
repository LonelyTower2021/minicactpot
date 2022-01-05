import json

def calculate_payout(value):
    with open('payout.json', 'r') as json_fp:
        payout = json.load(json_fp)
        return payout[f'{value}']

def get_payout(chosen_row):
    return calculate_payout(sum(chosen_row))

def possible_values(known_values):
    return set(range(1, 10)).difference(known_values)

def average_payout(chosen_row, known):
    unknown_num_pool = possible_values(known)
    num_cells = len(chosen_row)

    if num_cells > 3:
        raise ValueError("chosen_Row size must be less than or equal to 3")

    total = hidden_cells(chosen_row, unknown_num_pool)
    choose = 3 - len(chosen_row)
    combos = get_total_permutations(len(unknown_num_pool), choose)

    return total / combos

def get_total_permutations(num_obj, num_choice=1):
    import math
    n = math.factorial(num_obj)
    n_r = math.factorial(num_obj - num_choice)
    return n / n_r

def hidden_cells(chosen_row, unknown_num_pool):
    chosen_list = list(chosen_row)
    if len(chosen_row) == 3:
        return get_payout(chosen_row)
    else:
        import copy
        total = 0.0

        for unknown in unknown_num_pool:
            new_row = copy.deepcopy(chosen_list)
            new_pool = copy.deepcopy(unknown_num_pool)

            new_row.append(unknown)
            new_pool.remove(unknown)
            total += hidden_cells(new_row, new_pool)

        return total
