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
        json_file = "kanji.json"
        kanjis = load_json_to_list(json_file)
        print("Select your jlpt level", end=": ")
        level = int(input().strip())
        start_index = 0
        end_index = 2136
        if level == 5:
            end_index = 103
        elif level == 4:
            start_index = 103
            end_index = 284
        elif level == 3:
            start_index = 284
            end_index = 608
        elif level == 2:
            start_index = 608
            end_index = 1023
        else:
            start_index = 1023

        to_remember = {}
        need_remeber = False
        print("Kanji baengkyoga hajimarimasu.")
        for i in range(start_index, end_index):
            print("=" * 10)
            print()
            print(kanjis[i]["kanji"])
            print("Shittemasu? (y/n)")
            print("Enter x to exit", end=": ")
            user_input = input().strip()
            if user_input == "x":
                print("exit wordbook")
                return
            if user_input == "n":
                print_kanji_info(kanjis[i])
                to_remember[i] = kanjis[i]
                need_remeber = True

        key_to_remove = []
        while need_remeber:
            for k, kanji in to_remember.items():
                print(kanji["kanji"])
                print_kanji_info(kanji)
                print("Shittemasu? (y/n)")
                print("Enter x to exit", end=": ")
                user_input = input().strip()
                if user_input == "x":
                    print("exit wordbook")
                    return
                if user_input == "n":
                    print_kanji_info(kanji)
                    key_to_remove.append(k)
            if len(key_to_remove) == 0:
                need_remeber = False
                print("No more review left")
            else:
                for key in key_to_remove:
                    to_remember.pop(key)
        print("Otsukaresamadeshita")

    except:
        print("Nanika matchigaeta")
        return


def newmain():
    try:
        json_file = "kanji.json"
        kanjis = load_json_to_list(json_file)
        if not isinstance(kanjis, list) or not all(
            isinstance(k, dict) and "kanji" in k for k in kanjis
        ):
            raise ValueError("Invalid JSON structure")

        print("Select your JLPT level", end=": ")
        level = int(input().strip())
        start_index, end_index = 0, len(kanjis)

        if level == 5:
            end_index = 103
        elif level == 4:
            start_index, end_index = 103, 284
        elif level == 3:
            start_index, end_index = 284, 608
        elif level == 2:
            start_index, end_index = 608, 1023
        else:
            start_index = 1023

        end_index = min(
            end_index, len(kanjis)
        )  # Ensure we don't exceed the list length

        to_remember = {}
        print("Kanji baengkyoga hajimarimasu.")
        for i in range(start_index, end_index):
            print("=" * 10)
            print()
            print(kanjis[i]["kanji"])
            print("Shittemasu? (y/n)")
            print("Enter x to exit", end=": ")
            user_input = input().strip()
            if user_input == "x":
                print("Exit wordbook")
                return
            elif user_input == "n":
                print_kanji_info(kanjis[i])
                to_remember[i] = kanjis[i]

        while to_remember:
            key_to_remove = []
            for k, kanji in list(to_remember.items()):
                print(kanji["kanji"])
                print_kanji_info(kanji)
                print("Shittemasu? (y/n)")
                print("Enter x to exit", end=": ")
                user_input = input().strip()
                if user_input == "x":
                    print("Exit wordbook")
                    return
                elif user_input == "y":
                    key_to_remove.append(k)

            for key in key_to_remove:
                to_remember.pop(key)

            if not to_remember:
                print("No more review left")

        print("Otsukaresamadeshita")

    except Exception as e:
        print(f"An error occurred: {e}")
        return


def print_kanji_info(kanji):
    print("한자", kanji["kanji"])
    print("기본정보", kanji["basic_info"])
    print("한자구조", kanji["kanji_structure"])
    print("음독", kanji["on_yomi_info"])
    print("훈독", kanji["kun_yomi_info"])


if __name__ == "__main__":
    newmain()
