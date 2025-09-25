#a
for i in range(0, 101, 10):
    print(i, end=' ')
print()
#b
for i in range(20, 0, -1):
    print(i, end=' ')
print()
#c
number_of_stars = int(input("Please input number of stars to print: "))
for i in range(number_of_stars):
    print("*", end=' ')
print()
#d
number_of_lines = int(input("Please input how many lines of stars: "))
for i in range(1, number_of_lines + 1):
    print("* " * i)
print()
