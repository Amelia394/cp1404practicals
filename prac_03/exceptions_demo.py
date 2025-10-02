"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Q1. When will a ValueError occur?
# A ValueError occurs when a value that isn't an integer eg. a or &
# Q2. When will a ZeroDivisionError occur?
# A ZeroDivisionError occurs when the denominator is set to zero
# Q3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes. You can check if the denominator is 0 before dividing. If it is, handle it by asking for another number or by printing an error message instead of dividing.

# Modified version that prevents ZeroDivisionError:
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Denominator cannot be zero")
except ValueError:
    print("Numerator and denominator must be valid integers!")