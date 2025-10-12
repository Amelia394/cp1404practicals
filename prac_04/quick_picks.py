#Amelia Wilson
"""
CP1404 Practical 4
quick_picks.py
"""
import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    """Ask the user how many quick picks to generate and display them."""
    try:
        number_of_picks = int(input("How many quick picks? "))
    except ValueError:
        print("Invalid input; please enter a number.")
        return
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))

def generate_quick_pick():
    """Generate one quick pick of 6 unique random numbers between MIN_NUMBER and MAX_NUMBER."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

main()