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


def read_and_save_json(input_file, output_file):
  """Reads a JSON file and saves it to another JSON file.

  Args:
    input_file: The path to the input JSON file.
    output_file: The path to the output JSON file.
  """

  with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

  with open(output_file, 'w') as f:
    json.dump(data, f, indent=4,ensure_ascii=False)

if __name__ == "__main__":
    # print("Run CsvToJson")
    # csv_file = "kanji_sub.csv"  # Replace with your CSV file path
    # json_file = "kanji_sub.json"  # Replace with your desired JSON output path
    # csv_to_json(csv_file, json_file)
    # print("Job Done Successfully.")
    read_and_save_json('kanji_references.json','kanji_references_new.json')
