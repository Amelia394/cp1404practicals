#Amelia Wilson
"""
CP1404/CP5632 Practical
Test SilverServiceTaxi
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Hummer", 200, 2)
taxi.start_fare()
taxi.drive(18)
fare = taxi.get_fare()
print(f"Fare for 18km: ${fare:.2f}")
expected_price = 1.23 * 2
print(taxi)
