import csv
from datetime import datetime

def log_violation(violation_type, plate):
    with open("logs/violations.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), violation_type, plate])
