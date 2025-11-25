#Amelia Wilson
"""
CP1404 Practical
SilverServiceTaxi class
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Taxi that charges more based on fanciness """
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        """Initialise class for fancier taxis."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Retrieves the fare price including flagfall."""
        base_fare = super().get_fare()
        return base_fare + self.flagfall

    def __str__(self):
        """Return a string representation of fare including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"