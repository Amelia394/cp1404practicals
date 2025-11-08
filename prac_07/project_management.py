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
            header = fh.readline()
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("\t")

                name, start_date_str, priority, cost_estimate, completion = parts
                start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
                projects.append(Project(name, start_date, int(priority),
                                        float(cost_estimate), int(completion)))
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty project list.")
    return projects

def save_projects(filename, projects):
    """Save projects to filename."""
    with open(filename, "w") as fh:
        fh.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
        for p in projects:
            fh.write(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t"
                     f"{p.priority}\t{p.cost_estimate}\t{p.completion}\n")
    print(f"Saved {len(projects)} projects to {filename}")

def display_projects(projects):
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")

def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ").strip()
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return
    filtered = [p for p in projects if p.start_date >= filter_date]
    for p in sorted(filtered):
        print(p)

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ").strip()
    start_date_str = input("Start date (dd/mm/yyyy): ").strip()
    try:
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format; project not added.")
        return
    priority = int(input("Priority: ").strip())
    cost_estimate = float(input("Cost estimate: $").strip())
    completion = int(input("Percent complete: ").strip())
    projects.append(Project(name, start_date, priority, cost_estimate, completion))
    print("Project added.")

def main():
    filename = FILENAME
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    while True:
        print(MENU)
        choice = input(">>> ").strip().lower()
        if choice == "q":
            print("Goodbye")
            break
        elif choice == "l":
            filename = input("Filename to load from: ").strip()
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "s":
            filename = input("Filename to save to: ").strip()
        elif choice == "d":
            display_projects(projects)
            save_projects(filename, projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        else:
            print("Feature not implemented yet.")



if __name__ == "__main__":
    main()