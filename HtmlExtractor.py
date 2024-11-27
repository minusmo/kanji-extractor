from bs4 import BeautifulSoup

# Assuming the HTML content is stored in a string named 'html_content'
# You can replace this with reading the HTML from a file:

# with open('your_html_file.html', 'r') as f:
#     html_content = f.read()

# Extract the information using regular expressions or string manipulation
# Here's a basic example using regular expressions:
import re


class HtmlExtractor:
    def __init__(self, html_content) -> None:
        self.soup = BeautifulSoup(html_content, "html.parser")

    def find_texts(self) -> dict:
        # Find the text containing the desired information
        text = self.soup.get_text()

        # Adjust the regular expressions as needed based on the exact format of your HTML
        # Find the h2 element within the element with id="head"
        h2_element = self.soup.find("div", id="head").find("h2")

        # Extract the text from the h2 element
        h2_text = h2_element.text.strip()

        basic_info = (
            re.search(r"기본 정보(.*?)한자 모양 해설", text, re.DOTALL).group(1).strip()
        )
        kanji_structure = (
            re.search(r"한자 모양 해설(.*?)음독 상세", text, re.DOTALL).group(1).strip()
        )
        on_yomi_info = (
            re.search(r"음독 상세(.*?)훈독 상세", text, re.DOTALL).group(1).strip()
        )
        kun_yomi_info = (
            re.search(r"훈독 상세(.*?)5. 비고, 관련 링크", text, re.DOTALL)
            .group(1)
            .strip()
        )

        # Print the extracted information
        # print("한자:", h2_text)
        # print("기본 정보:", basic_info)
        # print("한자 모양 해설:", kanji_structure)
        # print("음독 상세:", on_yomi_info)
        # print("훈독 상세:", kun_yomi_info)
        return {
            "kanji": h2_text,
            "basic_info": basic_info,
            "kanji_structure": kanji_structure,
            "on_yomi_info": on_yomi_info,
            "kun_yomi_info": kun_yomi_info,
        }
