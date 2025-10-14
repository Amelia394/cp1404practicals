# Amelia Wilson
"""
CP1404 Practical 4
list_exercises.py
ask user for 5 numbers print first number, last number, smallest number, largest number and the average
ask user for username, check if username is in given list if it is access granted otherwise access denied
"""

def main():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers)*5 / len(numbers)}")
main()

usernames = [
    'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
    'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
    'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'
]

username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
