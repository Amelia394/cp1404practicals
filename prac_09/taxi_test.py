#Write lines of code for each of the following (hint: use the methods available in the Taxi class):
#Restart the meter (start a new fare) and then drive the car 100 km
#Print the details and the current fare

#Amelia Wilson
"""CP1404 Practical 09 taxi_test.py """

from prac_09.taxi import Taxi

my_taxi = Taxi('Prius 1', 100)

my_taxi.drive(40)
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")