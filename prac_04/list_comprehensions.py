#Amelia Wilson
"""
CP1404 Practical 4
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# For loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# List comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# List comprehension that creates a list containing the initials
# This splits each full name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# This example uses filtering to select only the names that start with 'A'
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# Example of using the join method to create a single string from sorted names
# Output example: 'Ada Alan Angel Bob Jimi'
print(" ".join(sorted(names)))

# List comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']

# List comprehension to create a list of integers from the above list of strings
numbers = [int(num) for num in almost_numbers]
print(numbers)

# List comprehension to create a list of only the numbers greater than 9
greater_than_nine = [num for num in numbers if num > 9]
print(greater_than_nine)

# More advanced: use a list comprehension and the join string method
# to create a string of the last names for those full names longer than 11 characters
# The result should be: 'Harlem, Hendrix, Lovelace'
long_last_names = ", ".join([name.split()[1] for name in full_names if len(name) > 11])
print(long_last_names)