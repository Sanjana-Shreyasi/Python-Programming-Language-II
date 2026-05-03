#U4Q13
#Write a Python program to convert the JSON array into a CSV file.
import json
import csv

# Read JSON file
with open("data.json", "r") as f:
    data = json.load(f)   # JSON array (list of dictionaries)

# Write to CSV file
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # Write header
    writer.writerow(data[0].keys())

    # Write rows
    for row in data:
        writer.writerow(row.values())

print("JSON converted to CSV successfully.")