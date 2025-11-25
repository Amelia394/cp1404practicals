#Amelia Wilson
"""
Taxi Simulator
CP1404 Practical
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    print("Let's drive!")
    taxis = [ Taxi("Prius", 100),SilverServiceTaxi("Limo", 100, 2),SilverServiceTaxi("Hummer", 200, 4) ]
    current_taxi = None
    bill_to_date = 0

    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)

            try:
                taxi_choice = int(input("Choose taxi: "))
                if taxi_choice < 0 or taxi_choice >= len(taxis):
                    print("Invalid taxi choice")
                else:
                    current_taxi = taxis[taxi_choice]
                    current_taxi.start_fare()
            except ValueError:
                print("Invalid input")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    bill_to_date += trip_cost
                except ValueError:
                    print("Invalid distance")

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Print each taxi with index."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()