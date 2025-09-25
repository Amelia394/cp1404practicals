# Amelia Wilson
"""
CP1404/CP5632 - Practical
Menu-driven program for working with scores
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Main program to display menu and handle options"""
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print("*" * score)
        elif choice == "Q":
            print("Farewell! Thanks for using the score menu program.")
        else:
            print("Invalid choice")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive"""
    score = int(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score (0-100): "))
    return score


def determine_result(score):
    """Return result string based on score value (does not print)"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"





main()