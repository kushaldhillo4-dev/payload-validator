import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 2:
    print("Usage: python check_xml.py <file.xml>")
    sys.exit(1)

try:
    root = ET.parse(sys.argv[1]).getroot()
except ET.ParseError as e:
    print(f"XML is malformed: {e}")
    sys.exit(1)

bad = 0
for s in root.findall("shipment"):
    sid = s.get("id")
    problems = []
    for tag in ("drug", "quantity", "destination"):
        el = s.find(tag)
        if el is None:
            problems.append(f"missing <{tag}> tag")
        elif not (el.text or "").strip():
            problems.append(f"<{tag}> is empty")
    qty = s.find("quantity")
    if qty is not None and (qty.text or "").strip() and not qty.text.strip().isdigit():
        problems.append("quantity is not a number")
    if problems:
        bad += 1
        print(f"{sid}: " + ", ".join(problems))

print(f"\nDone: {bad} bad shipment(s) found.")