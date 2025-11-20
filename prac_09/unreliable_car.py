#Amelia Wilson
"""
CP1404 Practical 09 unreliable_car.py
"""

from prac_09.car import Car

class UnreliableCar(Car):
    """Different version of car that has a reliability value."""

    def __init__(self, name, fuel, reliability):
        """Set up unreliable car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car."""