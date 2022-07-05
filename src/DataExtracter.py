from bs4 import BeautifulSoup as bs
import requests
import sys
sys.path.append("/src")
from MatchStatsStructure import MatchStatusStructure

class DataExtracter:

    structure = any
    
    def __init__(self):
        url = "https://understat.com/match/17124"
        response = requests.get(url)
        soup = bs(response.content, "html.parser")
        stats = soup.find_all("div", class_="progress-value")        
        i = 0
        while i in range(len(stats)):
            stats[i] = stats[i].text
            i += 1
        self.structure = MatchStatusStructure(stats)
