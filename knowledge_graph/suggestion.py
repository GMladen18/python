import requests

import xml.etree.ElementTree as ET
AUTO_COMPLETE = "http://suggestqueries.google.com/complete/search?&output=toolbar&gl=us&hl=en&q="


class Suggestion:
    def __init__(self, term):
        self.__term = term

    def get_suggestion(self):
        searched_term = f"{self.__term}%20vs%20"
        response = requests.get(AUTO_COMPLETE + searched_term)
        root = ET.fromstring(response.content)
        for element in root:
            value = element[0].attrib["data"]
            yield value


if __name__ == "__main__":
    term = input()
    suggestions = Suggestion(term)
    for suggestions in suggestions.get_suggestion():
        print(suggestions)
