# Amelia Wilson
"""
CP1404 Practical 6
guitar_test.py
estimate: 40 min
actual:34 min
"""

from prac_06.guitar import Guitar


def main():
    """Store and display users guitars."""
    print("My guitars!")

    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added")

        name = input("Name: ")

    if not guitars:
        print("No guitars.")
        return

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
#:10 reserves 10 character spaces (for alignment)
#,.2f → includes commas and always shows 2 decimal places

if __name__ == "__main__":
    main()
