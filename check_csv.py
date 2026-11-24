import csv
import sys

if len(sys.argv) != 2:
    print("Usage: python check_csv.py <file.csv>")
    sys.exit(1)

path = sys.argv[1]
bad_rows = 0

with open(path, newline="") as f:
    reader = csv.DictReader(f)
    for line_no, row in enumerate(reader, start=2):
        problems = []
        for field, value in row.items():
            if value is None or value.strip() == "":
                problems.append(f"missing {field}")
        qty = (row.get("quantity") or "").strip()
        if qty and not qty.isdigit():
            problems.append("quantity is not a number")
        if problems:
            bad_rows += 1
            print(f"Line {line_no} ({row['shipment_id']}): " + ", ".join(problems))

print(f"\nDone: {bad_rows} bad row(s) found.")