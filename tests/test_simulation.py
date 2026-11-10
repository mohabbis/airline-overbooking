from simulation import calculate_profit

def test_profit_with_bumped_passengers():
    profit = calculate_profit(105, 103, 100, 200, 400)
    assert profit == 19800


def test_profit_with_empty_seats():
    profit = calculate_profit(105, 95, 100, 200, 400)
    assert profit == 21000


def test_profit_with_exact_capacity():
    profit = calculate_profit(100, 100, 100, 200, 400)
    assert profit == 20000

import random
from simulation import simulate_arrivals


def test_zero_no_show_probability():
    rng = random.Random(42)
    arrivals = simulate_arrivals(105, 0.0, rng)
    assert arrivals == 105


def test_full_no_show_probability():
    rng = random.Random(42)
    arrivals = simulate_arrivals(105, 1.0, rng)
    assert arrivals == 0


def test_zero_tickets_sold():
    rng = random.Random(42)
    arrivals = simulate_arrivals(0, 0.10, rng)
    assert arrivals == 0


def test_same_seed_same_arrivals():
    rng1 = random.Random(42)
    rng2 = random.Random(42)

    arrivals1 = simulate_arrivals(105, 0.10, rng1)
    arrivals2 = simulate_arrivals(105, 0.10, rng2)

    assert arrivals1 == arrivals2
