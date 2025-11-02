#Amelia Wilsin
"""
CP1404 - Practical 6
programing_language.py
Estimate:45min
Actual: 1 hr
"""

class ProgrammingLanguage:
    """Represents ProgramingLanguage as an object."""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Returns sting for the Programing Language"""
        return f"{self.name}, Typing = {self.typing}, Reflection = {self.reflection}, Year = {self.year}"

    def is_dynamic(self):
        """Set typing to dynamic."""
        return self.typing.lower() == "Dynamic"

