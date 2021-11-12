def payout(selection):
    return sum(selection)

def odds(pool):
    return 1 / len(pool)

def possible(selection):
    return set(range(10)).difference(selection)
