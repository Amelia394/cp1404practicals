#Amelia Wilson
"""
CP1404 Practical 5
Wimbledon data-reading, processing and displaying
Estimate: 40 mins
Actual:
"""

FILENAME = "wimbledon.csv"

def load_records(filename):
    """Load records from file in list of lists form."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove CSV header row
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records