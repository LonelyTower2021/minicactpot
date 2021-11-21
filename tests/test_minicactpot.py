"""
Final Fantasy has a mini-lottery game called Mini Cactpot where the
player is presented with a 3x3 grid of hidden numbers.  The game
randomly chooses a cell to reveal, and gives the player three
opportunities to select three additional cells to unveil.

Afterwards, the player must select a row, column, or diagonal.  The
sum of those three numbers will determine the prize the player wins.

Breakdown:
    1. Computer reveals one cell
    2. Player reveals three cells
        a. Which cells should I reveal for the most information?
    3. Player selects either a row, column, or diagonal
        a. Which choice will give me the highest average payout?
    4. Computer reveals all unveiled cells of Player selection
    5. Computer calculates prize

Questions:
    1. Given a row of one unknowns, what are the odds of a certain value?
    2. Given a row of two unknowns, what are the odds of a certain value?
"""
from minicactpot import minicactpot
import pytest


def test_calculate_payout():
    selected_row = {1, 2, 3}
    expected = 10000
    actual = minicactpot.get_payout(selected_row)
    assert actual == expected

def test_get_possible_values():
    visible_cells = {2, 3, 7, 8}
    expected = {1, 4, 5, 6, 9}
    actual = minicactpot.possible(visible_cells)
    assert actual == expected

def test_calculate_odds_with_one_hidden_cells():
    possible_values = len([3, 4, 6, 7, 9])
    hidden_cells = 1
    expected = 1 / possible_values
    actual = minicactpot.odds(possible_values, hidden_cells)
    assert actual == expected

def test_calculate_odds_with_two_hidden_cells():
    possible_values = len([3, 4, 6, 7, 9])
    hidden_cells = 2
    expected = 1 / calculate_num_distinct_pairs(possible_values)
    actual = minicactpot.odds(possible_values, hidden_cells)
    assert actual == expected

def test_one_hidden_calculate_average_payout():
    selected_row = {2, 3}
    visible_cells = {2, 3, 5, 6, 7, 8, 9}
    expected = 5180.0
    actual = minicactpot.average_payout(selected_row, visible_cells)
    assert actual == expected

def test_two_hidden_calculate_average_payout():
    selected_row = {3}
    visible_cells = {3, 5, 6, 7, 8, 9}
    expected = 3693.33
    actual = minicactpot.average_payout(selected_row, visible_cells)
    assert actual == pytest.approx(expected)


def calculate_num_distinct_pairs(n):
    return (n * (n - 1)) / 2