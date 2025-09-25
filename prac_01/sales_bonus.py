# Amelia Wilson#
"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

"""
# input sales amount
sales = float(input("Enter sales: $"))

#loop until a negative value has been input
while sales >= 0:
    # calculating bonus based on sales
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15
    #print bonus
    print(f"Bonus: ${bonus:.2f}")
    # input sales amount
    sales = float(input("Enter sales: $"))

print("invalid sales input")
