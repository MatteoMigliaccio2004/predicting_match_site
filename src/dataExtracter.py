from bs4 import BeautifulSoup as bs
from h11 import Data
import requests

class DataExtracter:
    matches_stats = []
    url = "https://understat.com/match/17124"

    def get_stats(self):
        response = requests.get(self.url)
        soup = bs(response.content, "html.parser")
        stats = soup.find_all("div", class_="progress-value")        
        
some = DataExtracter()

some.get_stats()