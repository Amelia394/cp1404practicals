#Amelia Wilsin
"""
CP1404 - Practical 6
programming_language.py
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
        return self.typing == "Dynamic"

def run_tests():
    """Run test version."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    cpp = ProgrammingLanguage("C + +", "Static", False, 1993)
    java = ProgrammingLanguage("Java", "Static", True, 1995)

    languages = [ruby, python, visual_basic, cpp, java]
    print(python)

    print("The dynamic languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()