import json

# kanji_data = [
#     {
#         "kanji": "",
#         "basic_info": "",
#         "kanji_structure": "",
#         "on_yomi_info": "",
#         "kun_yomi_info": "",
#     }
# ]


def load_json_to_list(json_file_path):
    try:
        with open(json_file_path, mode="r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                print("Kanji loading complete.")
                return data
            else:
                raise ValueError("The JSON file is wrong.")
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None


def main():
    try:
        json_file = "kanji.json"  # Replace with your JSON file path
        print("Getting kanji list")
        kanjis = load_json_to_list(json_file)
        to_remember = {}
        print("Kanji baengkyoga hajimarimasu.")
        for kanji in kanjis:
            print(kanji["kanji"])
            print("Knew? (y/n)")
            print("enter x to exit", end=" ")
            user_input = input().strip()
            if user_input == "x":
                print("exit wordbook")
                return
            if user_input == "n":
                print_kanji_info(kanji)
                to_remember[kanji["kanji"]] = kanji

        while len(to_remember) != 0:
            for kanji in to_remember:
                print(kanji["kanji"])
                print_kanji_info(kanji)
                print("Shittemasu? (y/n)")
                print("enter x to exit", end=" ")
                user_input = input().strip()
                if user_input == "x":
                    print("exit wordbook")
                    return
                if user_input == "n":
                    print_kanji_info(kanji)
                else:
                    to_remember.pop(kanji["kanji"])
        print("Otsukaresamadeshita")

    except:
        print("Nanika matchigaeta")
        return


def print_kanji_info(kanji):
    print("한자", kanji["kanji"])
    print("기본정보", kanji["basic_info"])
    print("한자구조", kanji["kanji_structure"])
    print("음독", kanji["on_yomi_info"])
    print("훈독", kanji["kun_yomi_info"])


if __name__ == "__main__":
    main()
