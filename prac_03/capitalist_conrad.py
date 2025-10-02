# Amelia Wilson
"""
CP1404 - Practical 3
Capitalist Conrad - Stock Price Simulator
Simulates the price of a volatile stock, starting at $10.00.
- At the end of each day, there is a 50% chance the price increases
  by up to 17.5%, or decreases by up to 5%.
- The program ends if the price goes below $1.00 or above $100.00.
- The daily prices are written to an output file.
"""

import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_prices.txt"


def main():
    """Simulate stock price changes and write results to file."""
    price = INITIAL_PRICE
    number_of_days = 0

    with open(OUTPUT_FILE, 'w') as out_file:
        print(f"Starting price: ${price:,.2f}", file=out_file)

        while MIN_PRICE <= price <= MAX_PRICE:
            number_of_days += 1
            price_change = get_price_change()
            price *= (1 + price_change)
            print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)


def get_price_change():
    """Determine a random daily price change."""
    if random.randint(1, 2) == 1:
        return random.uniform(0, MAX_INCREASE)  # price increases
    else:
        return random.uniform(-MAX_DECREASE, 0)  # price decreases

    main()
