#Amelia Wilson
"""CP1404 - Practical 2
Convert an input password to * for the length of the password
"""

MINIMUM_LENGTH = 6

def main():
    """Get password and print asterisks using functions"""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Ask user for a password until minimum length requirement is met"""
    print(f"Remember your password must be at least {MINIMUM_LENGTH} characters long")
    password = input("Please enter your password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password isn't long enough please try again.")
        print(f"Your password has to be at least {MINIMUM_LENGTH} letters")
        password = input("Please enter your password: ")
    return password

def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print("*"*len(password))

main()
