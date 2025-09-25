#Amelia Wilson
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

#input score
score = float(input("Enter score: "))
#is it within the bounds 0-100?
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
#issue with previous code was multiple if statements were causing issues