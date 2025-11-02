#Amelia Wilson
"""
CP1404 - Practical 6
languages.py
Estimate: 45 min
Actual: 1 hr
"""

from prac_06.programming_language import ProgrammingLanguage
def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    cpp = ProgrammingLanguage("C + +","Static",False,1993)
    java = ProgrammingLanguage("Java","Static", True, 1995)


    languages = [ruby, python, visual_basic, cpp, java]
    print("The dynamic languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()

