# Amelia Wilson
"""
CP1404 - Practical 3
Capitalist Conrad - Stock Price Simulator
The price starts off at $10.00, and at the end of every day there is
a 50% chance it increases by up to 17.5%, and
a 50% chance that it decreases by up to 5%.
If the price rises above $100, or falls below $1, the program ends.
The price should be displayed to the nearest cent and output is written to a file.
"""

import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_prices.txt"

out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
number_of_days = 0
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    if random.randint(1, 2) == 1:
        # price increases
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # price decreases
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()