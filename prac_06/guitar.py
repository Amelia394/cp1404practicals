#Amelia Wilson
"""
CP1404 Practical 6
guitar.py
estimate: 40 min
actual:
"""

class Guitar:
    """Represents guitar as a class."""
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
    def __str__(self):
        """Returns sting for the Guitar."""
        return f"{self.name} ({self.year}): ${self.cost}."