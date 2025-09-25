# Amelia Wilson

print("Welcome to the classroom sequence generator")
# get x and y values
def get_range():
    x_value = int(input("Enter the starting number (x): "))
    y_value = int(input("Enter the ending number (y): "))
    return x_value, y_value

# Initial x and y input
x, y = get_range()

# menu driven
def display_menu():
    print("\nMenu:")
    print("1. Show the even numbers from x to y")
    print("2. Show the odd numbers from x to y")
    print("3. Show the squares of the numbers from x to y")
    print("4. Set new x and y values")
    print("5. Exit the program")


# Display menu
display_menu()

choice = input(">>> ")
#start loop until option 5 is chosen
while choice != "5":
    #show the even numbers from x to y
    if choice == "1":
        for number in range(x, y + 1):
            if number % 2 == 0:
                print(number, end=" ")
        print()
    #show the odd numbers from x to y
    elif choice == "2":
        for number in range(x, y + 1):
            if number % 2 != 0:
                print(number, end=" ")
        print()
    # Show the squares of the numbers from x to y
    elif choice == "3":
        for number in range(x, y + 1):
            print(number ** 2, end=" ")
        print()
    #added extra choice to change x and y values
    elif choice == "4":
        x, y = get_range()
    #any other option is invalid
    else:
        print("Invalid choice")
    #repeat
    display_menu()
    choice = input(">>> ")
#stop loop after option 5 is chosen
print("Thanks for playing! :)")
