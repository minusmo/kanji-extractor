import csv
import json


def csv_to_json(csv_file_path, json_file_path):
    try:
        # Read the CSV file
        with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # Convert rows to a list of dictionaries
            data = [row for row in csv_reader]

        # Write the data to a JSON file
        with open(json_file_path, mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print(f"JSON file created successfully: {json_file_path}")
    except Exception as e:
        print(f"Error converting CSV to JSON: {e}")


# Example usage


if __name__ == "__main__":
    print("Run CsvToJson")
    csv_file = "kanji_n1.csv"  # Replace with your CSV file path
    json_file = "kanji_n1.json"  # Replace with your desired JSON output path
    csv_to_json(csv_file, json_file)
    print("Job Done Successfully.")
