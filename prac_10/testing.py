# Amelia Wilson
"""
CP1404 Practical 10
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)
def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length
def format_sentence(phrase):
    """
    Format a phrase as a sentence starting with a capital
    and ending with one full stop.
    """
    phrase = phrase.strip()
    if not phrase:
        return "."
    phrase = phrase.rstrip(".")
    parts = phrase.split(" ", 1)
    first_word = parts[0].capitalize()
    if len(parts) > 1:
        rest = parts[1]
        return f"{first_word} {rest}."
    else:
        return first_word + "."
def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"
    car = Car()
    assert car._odometer == 0, "Car doesn't set odometer"
    car = Car()
    assert car.fuel == 0, "Car default fuel isn't set right"
    car = Car(fuel=10)
    assert car.fuel == 10, "Car fuel (10) not set correctly"
run_tests()

doctest.testmod()