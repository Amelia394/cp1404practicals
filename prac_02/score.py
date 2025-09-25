#Amelia Wilson
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    """Get score and print result"""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

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
