#Amelia Wilson
"""
CP1404 Practical 6
guitar.csv.py
estimate: 40 min
actual: 34 min
"""

class Guitar:
    """Represents guitar.csv as a class."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
    def __str__(self):
        """Returns sting for the Guitar."""
        return f"{self.name} ({self.year}): ${self.cost}."

    def get_age(self):
        """Return age of guitar.csv."""
        current_year = 2025
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar.csv is 50 or more years old."""
        return self.get_age() >= 50