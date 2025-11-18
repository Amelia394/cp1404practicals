#Write lines of code for each of the following (hint: use the methods available in the Taxi class):
#Print the taxi's details and the current fare
#Restart the meter (start a new fare) and then drive the car 100 km
#Print the details and the current fare

#Amelia Wilson
""" """

from prac_09.taxi import Taxi

my_taxi = Taxi('Prius 1', 100, 1.23)
Taxi.drive(my_taxi, 40)
print(my_taxi)
