"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    input_file = open(FILENAME)
    subject_details = load_subject_details(input_file)
    input_file.close()
    print(subject_details)


def load_subject_details(input_file):
    """Read data from file formatted like: subject, lecturer, number of students."""
    subjects = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])  # Convert number of students to int
        subjects.append(parts)
    return subjects


main()