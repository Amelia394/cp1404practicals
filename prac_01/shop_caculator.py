#Amelia Wilson

total_price = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
#The program allows the user to enter the number of items and the price of each different item.
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price
#If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
if total_price > 100:
    total_price *= 0.9
#Then the program computes and displays the total price of those items.
print(f"Total price for {number_of_items} items is ${total_price:.2f}")