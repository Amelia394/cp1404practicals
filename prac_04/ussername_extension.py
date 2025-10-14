# Amelia Wilson
"""
CP1404/CP5632 Practical Extension
Username and Password Authorisation System

This program allows users to:
1. Create strong passwords for a set of predefined usernames.
2. Then log in by entering a username and matching password.

Password requirements:
- At least 8 characters long
- At least 2 digits
- At least 1 uppercase letter
- At least 1 special character (e.g. !@#$%^&*)
"""

import string

# Predefined authorised usernames
USERNAMES = [
    'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
    'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
]


def main():
    """Main program: setup passwords and then log in."""
    print("=== Password Setup ===")
    user_passwords = create_passwords()

    print("\n=== Login System ===")
    login(user_passwords)


def create_passwords():
    """
    Prompt the user to create passwords for each username.
    Passwords must meet the strength requirements.
    Returns a dictionary mapping usernames to passwords.
    """
    user_passwords = {}

    for username in USERNAMES:
        print(f"\nCreate a password for '{username}'")
        password = input("Enter password: ")
        while not is_valid_password(password):
            print("Invalid password! It must be at least 8 characters long, "
                  "contain 2 digits, 1 uppercase letter, and 1 special character.")
            password = input("Enter password: ")
        user_passwords[username] = password
    print("\nAll passwords set successfully!")
    return user_passwords


def is_valid_password(password):
    """Check if the password meets the defined strength requirements."""
    if len(password) < 8:
        return False

    digit_count = sum(char.isdigit() for char in password)
    uppercase_count = sum(char.isupper() for char in password)
    special_count = sum(char in string.punctuation for char in password)

    return digit_count >= 2 and uppercase_count >= 1 and special_count >= 1


def login(user_passwords):
    """Prompt user for username and password and verify access."""
    username = input("Enter your username: ")

    if username not in user_passwords:
        print("Access denied: username not recognised.")
        return

    password = input("Enter your password: ")
    if user_passwords[username] == password:
        print("Access granted.")
    else:
        print("Access denied: incorrect password.")
main()
