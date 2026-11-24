# Payload Validator

Python scripts that validate shipment data files and report bad records.

- check_csv.py: finds missing fields and non-numeric quantities in a CSV file
- check_xml.py: finds missing or empty tags, non-numeric quantities and malformed XML

Usage:
python check_csv.py shipments.csv
python check_xml.py shipments.xml

The sample files (shipments.csv, shipments.xml) contain deliberate errors for testing.