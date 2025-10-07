"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    """Read subject data from file and display subject details."""
    input_file = open(FILENAME)
    subject_details = load_subject_details(input_file)
    input_file.close()
    display_subject_details(subject_details)

def load_subject_details(input_file):
    """Read data from file formatted like: subject, lecturer, number of students."""
    subjects = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])  # Convert number of students to int
        subjects.append(parts)
    return subjects

def display_subject_details(subject_details):
    """Display subject information neatly."""
    for subject in subject_details:
        subject_code = subject[0]
        lecturer = subject[1]
        num_students = subject[2]
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")

main()
