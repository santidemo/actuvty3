import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())  # Escribir las cabeceras
        for row in data:
            writer.writerow(row.values())

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)