from HtmlExtractor import HtmlExtractor
import requests
import csv

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


blank_info = {
    "kanji": "",
    "basic_info": "",
    "kanji_structure": "",
    "on_yomi_info": "",
    "kun_yomi_info": "",
}


def extract_kanji_contents(page_index) -> dict:
    target_page = f"https://nihongokanji.com/{page_index}"
    html_content = requests.get(target_page)
    try:
        html_extractor = HtmlExtractor(html_content.text)
        return html_extractor.find_texts()
    except:
        print("page error: ", page_index)
        return blank_info


def main():
    csv_file = "kanji_n1.csv"
    kanji_info_collection = []
    for page_idx in range(1036, 2149):
        print("current_page: ", page_idx)
        kanji_contents = extract_kanji_contents(page_idx)
        if len(kanji_contents.get("kanji")) == 0:
            continue
        kanji_info_collection.append(kanji_contents)
    create_csv_file(kanji_info_collection, csv_file)
    print("job done.")


if __name__ == "__main__":
    main()
