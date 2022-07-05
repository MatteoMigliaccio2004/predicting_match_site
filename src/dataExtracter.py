from bs4 import BeautifulSoup as bs
import requests
import sys
sys.path.append("/src")
from MatchStatsStructure import MatchStatusStructure

class DataExtracter:
    matches_stats = []
    url = "https://understat.com/match/17124"
    structure = any
    
    def __init__(self):
        response = requests.get(self.url)
        soup = bs(response.content, "html.parser")
        stats = soup.find_all("div", class_="progress-value")        
        i = 0
        while i in range(len(stats)):
            stats[i] = stats[i].text
            i += 1
        self.structure = MatchStatusStructure(stats)
    
#prova = DataExtracter()
#stampa = prova.structure.get_match()
#print(stampa)
