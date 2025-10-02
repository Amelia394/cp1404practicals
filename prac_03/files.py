#Amelia Wilson
"""
CP1404 Practical 3
files.py

"""
# 1. Ask user for name, write to name.txt
name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

# 2. Read the name from name.txt and print greeting
file = open("name.txt", "r")
saved_name = file.read().strip()  # Remove any extra whitespace
file.close()
print(f"Hi {saved_name}!")

# 3. Read first two numbers from numbers.txt and add them
with open("numbers.txt", "r") as file:
    first = int(file.readline().strip())
    second = int(file.readline().strip())
    print(first + second)  # Should print 59

# 4. Sum all numbers in numbers.txt
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(total)