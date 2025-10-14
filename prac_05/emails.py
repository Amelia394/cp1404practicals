#Amelia Wilson
"""
CP1404 Practical 4
email.py
Estimated: 35 mins
Actual: mins
"""

def main():
    """Store users' emails and names, then display them."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def extract_name(email):
    """Extract a likely name from the email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

    main()