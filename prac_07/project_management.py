#Amelia Wilson
"""
CP1404 practical 7
project_management.py
estimate: 40 mins
actual:
"""

from project import Project
from datetime import datetime

FILENAME = "projects.txt"

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""

def load_projects(filename):
    """Load projects and return a list of Projects."""
    projects = []
    try:
        with open(filename, "r") as fh:
            header = fh.readline()  # skip header
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("\t")
                # expected: name, start_date_str (dd/mm/YYYY), priority, cost_estimate, completion
                name, start_date_str, priority, cost_estimate, completion = parts
                start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
                projects.append(Project(name, start_date, int(priority),
                                        float(cost_estimate), int(completion)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty project list.")
    return projects

def main():
    print("Welcome to Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    while True:
        print(MENU)
        choice = input(">>> ").strip().lower()
        if choice == "q":
            print("Goodbye")
            break
        else:
            print("Feature not implemented yet.")

if __name__ == "__main__":
    main()