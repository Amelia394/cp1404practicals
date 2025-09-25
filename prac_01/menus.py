#Amelia Wilson

# Get name
name = input("Enter name: ")

# Display menu function for reuse
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)

# Get initial choice
choice = input(">>> ").upper()  # Convert to uppercase so input is not case-sensitive
# Loop until user chooses to quit
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")

