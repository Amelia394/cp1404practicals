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
    """Stub: will load projects from filename (not implemented yet)."""
    return []

def main():
    print("Welcome to Pythonic Project Management")
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