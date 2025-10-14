#Amelia Wilson
"""
CP1404 Practical 5
Hexadecimal colour codes in a dictionary
"""

CODE_TO_COLOUR = {
    "RED": "#ff0000",
    "ORANGE": "#ff5800",
    "YELLOW": "#ffff00",
    "GREEN": "#00ff00",
    "BLUE": "#0000ff",
    "PURPLE": "#a020f0",
    "PINK": "#ffc0cb",
    "BLACK": "#000000",
    "WHITE": "#ffffff",
    "BROWN": "#a52a2a"
}
print(CODE_TO_COLOUR)

colour_name = input("Enter colour name: ").upper()
while colour_name != "":
    if colour_name in CODE_TO_COLOUR:
        print(f"{colour_name} is {CODE_TO_COLOUR[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter hexadecimal colour code: ").upper()
