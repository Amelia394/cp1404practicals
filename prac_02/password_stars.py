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
    """Ask user for a password untill minimum length requirement is met"""
    print(f"Remember your password must be at least {MINIMUM_LENGTH} charecters long")
    password = input("Please enter your password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password isn't long enough please try again.")
        print("Your password has to be at least 6 letters")
        password = input("Please enter your password: ")
    return password

def print_asterisks(password):
    print("*"*len(password))

main()
