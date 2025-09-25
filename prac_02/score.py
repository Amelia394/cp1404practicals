#Amelia Wilson
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def main():
    """Get random score and print result"""
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    print(determine_result(random_score))

def determine_result(score):
    """Return result string based on score value"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

main()