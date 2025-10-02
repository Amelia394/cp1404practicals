# Amelia Wilson
"""
CP1404 - Practical 3
Capitalist Conrad - Stock Price Simulator
Simulates the price of a volatile stock, starting at $10.00.
Writes daily stock prices to a file until the price is too high or too low.
"""

import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"


def main():
    """Simulate stock price changes and write results to file."""
    price = INITIAL_PRICE
    number_of_days = 0
    out_file = open(FILENAME, 'w')  # open once before the loop
    print(f"Starting price: ${price:,.2f}", file=out_file)
    while MIN_PRICE <= price <= MAX_PRICE:
        number_of_days += 1
        price_change = get_price_change()
        price *= (1 + price_change)
        print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)
    out_file.close()  # close at the end


def get_price_change():
    """Return a random daily price change (positive or negative)."""
    if random.randint(1, 2) == 1:
        return random.uniform(0, MAX_INCREASE)  # price increases
    else:
        return random.uniform(-MAX_DECREASE, 0)  # price decreases


main()
