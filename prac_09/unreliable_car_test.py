#Amelia Wilson
"""
CP1404 Practical 09 unreliable_car_test.py
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    """Test drivability of car through multiple attemps."""
    unreliable_car = UnreliableCar("Tesla", 200, 25)

    for i in range(1, 11):
        distance_attempted = 10
        distance_driven = unreliable_car.drive(distance_attempted)
        print(f"Attempt {i}: Tried to drive {distance_attempted}km — drove {distance_driven}km")

    print("Final car state:")
    print(unreliable_car)


main()