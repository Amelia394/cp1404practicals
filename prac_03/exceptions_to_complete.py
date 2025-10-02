"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # If conversion succeeds, exit the loop
        is_finished = True
    except ValueError:  # Catch the exception when input is not an integer
        print("Please enter a valid integer.")
print("Valid result is:", result)