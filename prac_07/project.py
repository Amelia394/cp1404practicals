#Amelia Wilson
"""
CP1404 practical 7
project.py
estimate: 40 mins
actual:
"""
from datetime import date

class Project:
    """Represent project as a class."""

    def __init__(self, name: str, start_date: date, priority: int,
                 cost_estimate: float, completion: int):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)

    def is_complete(self) -> bool:
        """Return True if the project is done."""
        return self.completion == 100

    def __str__(self) -> str:
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion}%")

    def __lt__(self, other):
        """Sort projects by priority level."""
        return self.priority < other.priority