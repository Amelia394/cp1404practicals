#Amelia Wilson
"""
CP1404 Practical 7
myguitars.py
estimate: 40 min
actual: 34 min
"""
from guitar import Guitar


def main():
    """Load guitars and print."""
    guitars = load_guitars("guitars.csv")

    print("These are your guitars:")
    for guitar in guitars:
        print(guitar)

    print("Add new guitars (blank name to stop):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")

    guitars.sort()

    print("All guitars (sorted by year):")
    for guitar in guitars:
        print(guitar)

    save_guitars("guitars.csv", guitars)

def load_guitars(filename):
    """Read file and return as list."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def save_guitars(filename, guitars):
    """Write guitars in a CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()