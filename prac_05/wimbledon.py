#Amelia Wilson
"""
CP1404 Practical 5
Wimbledon data-reading, processing and displaying
Estimate: 40 mins
Actual:
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2

def load_records(filename):
    """Load records from file in list of lists form."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove CSV header row
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records

def process_records(records):
    """Create dictionary of champions and set of countries from records (list of lists)."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        champion_to_count[record[INDEX_CHAMPION]] = (
            champion_to_count.get(record[INDEX_CHAMPION], 0) + 1
        )
    return champion_to_count, countries