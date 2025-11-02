#Amelia Wilson
"""
CP1404 Practical 6
guitar_test.py
estimate: 40 min
actual:
"""

from prac_06.guitar import Guitar

def main():
    """Store and display users guitars."""
    print("My guitars!")

    # Temporary test data (will replace with input soon)
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    # Display all guitars in list
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10}{vintage_string}")

if __name__ == "__main__":
    main()
