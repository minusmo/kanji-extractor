from HtmlExtractor import CommonUsedKanjiExtractor, SubKanjiExtractor
import requests
import csv, json

# sample_data = [
#     {
#         "kanji": "",
#         "basic_info": "",
#         "kanji_structure": "",
#         "on_yomi_info": "",
#         "kun_yomi_info": "",
#     }
# ]


def create_csv_file(data, file_path):
    if not data:
        print("No data to write.")
        return

    # Extract headers from the first dictionary's keys
    headers = data[0].keys()

    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"CSV file created successfully: {file_path}")
    except Exception as e:
        print(f"Error creating CSV file: {e}")


EMPTY_COMMON_KANJI = {
    "kanji": "",
    "basic_info": "",
    "kanji_structure": "",
    "on_yomi_info": "",
    "kun_yomi_info": "",
}

EMPTY_SUB_KANJI = {
    "kanji": "",
    "basic_info": "",
    "kanji_structure": "",
    "reference": ""
}


def extract_commonkanji_contents(page_index) -> dict:
    target_page = f"https://nihongokanji.com/{page_index}"
    html_content = requests.get(target_page)
    try:
        html_extractor = CommonUsedKanjiExtractor(html_content.text)
        return html_extractor.find_texts()
    except:
        print("page error: ", page_index)
        return EMPTY_COMMON_KANJI
      
def extract_subkanji_contents(page_index) -> dict:
    target_page = f"https://nihongokanji.com/{page_index}"
    html_content = requests.get(target_page)
    try:
        html_extractor = SubKanjiExtractor(html_content.text)
        return html_extractor.find_texts()
    except:
        print("page error: ")
        return EMPTY_SUB_KANJI

def save_to_json():
  # Specify the filename
  filename = 'kanji_references.json'
  kanji_info_collection = []
  for page_idx in range(0, 2137):
      print("current_page: ", page_idx)
      kanji_contents = extract_commonkanji_contents(page_idx)
      if len(kanji_contents.get("kanji")) == 0:
          print('passed on no kanji data')
          continue
      kanji_info_collection.append({
        "kanji": kanji_contents.get("kanji"),
        "reference": f"https://nihongokanji.com/{page_idx}"
        })
  # Write the list of dictionaries to a JSON file
  with open(filename, 'w') as file:
    json.dump(kanji_info_collection, file, indent=4)

    print(f"Data saved to {filename}")

def main():
    csv_file = "kanji_sub.csv"
    kanji_info_collection = []
    for page_idx in range(2151, 2317):
        print("current_page: ", page_idx)
        kanji_contents = extract_subkanji_contents(page_idx)
        if len(kanji_contents.get("kanji")) == 0:
            print('passed on no kanji data')
            continue
        kanji_contents["reference"] = f"https://nihongokanji.com/{page_idx}";
        kanji_info_collection.append(kanji_contents)
    create_csv_file(kanji_info_collection, csv_file)
    print("job done.")


if __name__ == "__main__":
    save_to_json()
