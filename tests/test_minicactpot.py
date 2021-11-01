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
    3. Player selects either a row, column, or diagonal
    4. Computer reveals all unveiled cells of Player selection
    5. Computer calculates prize
"""
from minicactpot import minicactpot


def test_calculate_payout():
    selected_row = [1, 2, 3]
    expected = sum(selected_row)
    actual = minicactpot.payout(selected_row)
    assert actual == expected

def test_calculate_odds():
    pool = [3, 4, 5, 6, 7, 8, 9]
    expected = 1 / len(pool)
    actual = minicactpot.odds(pool)
    assert actual == expected

