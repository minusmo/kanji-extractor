import json


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

jlpt_kanji_index_range = {
  "n5": {
    "start": 0,
    "end": 103
  },
  "n4": {
    "start": 103,
    "end": 284
  },
  "n3": {
    "start": 284,
    "end": 608
  },
  "n2": {
    "start": 608,
    "end": 1023
  },
  "n1": {
    "start": 1023,
    "end": 2136
  }
}

def main():
    try:
        json_file = "kanji.json"
        kanjis = load_json_to_list(json_file)
        if not isinstance(kanjis, list) or not all(
            isinstance(k, dict) and "kanji" in k for k in kanjis
        ):
            raise ValueError("Invalid JSON structure")

        print("JLPT 급수를 선택해주세요", end=": N")
        level = int(input().strip())
        start_index, end_index = 0, len(kanjis)

        if level == 5:
            end_index = jlpt_kanji_index_range["n5"]["end"]
        elif level == 4:
            start_index, end_index = jlpt_kanji_index_range["n4"]["start"], jlpt_kanji_index_range["n4"]["end"]
        elif level == 3:
            start_index, end_index = jlpt_kanji_index_range["n3"]["start"], jlpt_kanji_index_range["n3"]["end"]
        elif level == 2:
            start_index, end_index = jlpt_kanji_index_range["n2"]["start"], jlpt_kanji_index_range["n2"]["end"]
        else:
            start_index = jlpt_kanji_index_range["n1"]["start"]

        end_index = min(
            end_index, len(kanjis)
        )  # Ensure we don't exceed the list length

        to_remember = {}
        print("건너뛰어서 시작하시겠습니까?(y/n)", end=": ")
        answer = input().strip()
        if answer == "y":
          print(f"JLPT N{level} 한자는 {start_index+1}번부터 시작합니다.")
          print("건너뛰어서 시작할 번호 입력", end=": ")
          start_index = int(input().strip()) - 1
        
        print("한자공부를 시작합니다.")
        for i in range(start_index, end_index):
            print("=" * 20)
            print()
            print(kanjis[i]["kanji"])
            print("알고있습니까?(y/n)")
            print("x를 입력하면 종료합니다.", end=" ")
            user_input = input().strip()
            if user_input == "x":
                print("암기 종료")
                return
            elif user_input == "n":
                print_kanji_info(kanjis[i],i)
                to_remember[i] = kanjis[i]

        while to_remember:
            key_to_remove = []
            for k, kanji in list(to_remember.items()):
                print("=" * 20)
                print(kanji["kanji"])
                print_kanji_info(kanji,k)
                print("알고있습니까?(y/n)")
                print("x를 입력하면 종료합니다.", end=" ")
                user_input = input().strip()
                if user_input == "x":
                    print("암기 종료")
                    return
                elif user_input == "y":
                    key_to_remove.append(k)

            for key in key_to_remove:
                to_remember.pop(key)

            if not to_remember:
                print("남은 암기할 한자가 없습니다.")

        print("고생하셨습니다.")

    except Exception as e:
        print(f"An error occurred: {e}")
        return

index_page_index = [649,650,651,652,2285]

def get_page_index(kanji_index):
  """
  레퍼런스 사이트는 인덱스가 1부터 시작합니다.
  그리고 path_variable이 8부터 시작합니다.
  즉, 1번한자의 path_variable이 8입니다.
  """
  reference_site_index = kanji_index + 1
  if reference_site_index + 7 < 649:
    return f"https://nihongokanji.com/{reference_site_index + 8}"
  elif reference_site_index + 7 >= 649:
    return f"https://nihongokanji.com/{reference_site_index + 12}"
  else:
    return f"https://nihongokanji.com/{reference_site_index + 12}"

def print_kanji_info(kanji, kanji_index):
    print("#" * 20)
    print()
    print("한자: ", kanji["kanji"])
    print("기본정보: ", kanji["basic_info"])
    print("한자구조: ", kanji["kanji_structure"])
    print("음독: ", kanji["on_yomi_info"])
    print("훈독: ", kanji["kun_yomi_info"])
    print(f"설명이 부족하다면 원본 설명을 보세요: {get_page_index(kanji_index)}")
    print()
    print("#" * 20)


if __name__ == "__main__":
    main()
