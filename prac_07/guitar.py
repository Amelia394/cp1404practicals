#Amelia Wilson
"""
CP1404 Practical 6
guitar.csv.py
estimate: 40 min
actual: 34 min
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name, year, cost):
        """Show guitar class in terms of name, year and cost"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return guitar represented as a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get age of guitar."""
        return 2025 - self.year  # update year as needed

    def is_vintage(self):
        """Check if guitar is over 50 years old."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Define < operator for sorting by year."""
        return self.year < other.year