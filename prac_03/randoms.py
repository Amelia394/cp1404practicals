# Amelia Wilson
"""
CP1404 - Practical 3
randoms.py
Random function testing.
"""
import random


def main():
    """Demonstrate use of random functions with examples and answers in comments."""
    print(random.randint(5, 20))  # Line 1: randint includes both endpoints
    # smallest = 5, largest = 20
    print(random.randrange(3, 10, 2))  # Line 2: randrange with step=2 gives odd numbers between 3 and 9
    # smallest = 3, largest = 9, cannot be 4
    print(random.uniform(2.5, 5.5))  # Line 3: uniform returns float in range
    # smallest = 2.5, largest = 5.5
    # Extra: random number between 1 and 100 inclusive
    print(random.randint(1, 100))

    main()
