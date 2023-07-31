import csv

csv_file = "data.csv"

test = {
    "field 1": "hio",
    "field 2": "hi2"
}

field_names = ["field 1", "field 2"]
# Open the CSV file in append mode and write the new row
with open(csv_file, 'a', newline='') as f:
    writer = csv.DictWriter(f, field_names)

    # Write the new row (dictionary) to the CSV file
    writer.writerow(test)

print("Data appended to CSV:", csv_file)
