#Amelia Wilson
"""
CP1404 Practical 5
State names in a dictionary
File reformatted to follow PEP 8 conventions.
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "SA": "South Australia",
    "TAS": "Tasmania",
    "VIC": "Victoria",
    "ACT": "Australian Capital Territory"
}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
