#Amelia Wilson
"""
CP1404 Practical 5
Hexadecimal colour codes in a dictionary
"""

CODE_TO_COLOUR = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "SA": "South Australia",
    "TAS": "Tasmania",
    "VIC": "Victoria",
    "ACT": "Australian Capital Territory"
}
print(CODE_TO_COLOUR)

colour_code = input("Enter hexadecimal colour code: ").upper()
while colour_code != "":
    if colour_code in CODE_TO_COLOUR:
        print(f"{colour_code} is {CODE_TO_COLOUR[colour_code]}")
    else:
        print("Invalid hexadecimal colour code")
    colour_code = input("Enter hexadecimal colour code: ").upper()
