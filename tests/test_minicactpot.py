"""
Final Fantasy has a mini-lottery game called Mini Cactpot where the
player is presented with a 3x3 grid of hidden numbers.  The game
randomly chooses a cell to reveal, and gives the player three
opportunities to select three additional cells to unveil.

Afterwards, the player must select a row, column, or diagonal.  The
sum of those three numbers will determine the prize the player wins.
"""
from minicactpot import minicactpot


def test_calculate_payout():
    selected_row = [1, 2, 3]
    expected = sum(selected_row)
    actual = minicactpot.payout(selected_row)
    assert actual == expected
