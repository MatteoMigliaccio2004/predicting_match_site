import sys
sys.path.append("/src")
from DataExtracter import DataExtracter
from bs4 import BeautifulSoup as bs
import requests

class MatchResearcher:

    number_of_matches = 0
    home_team_name = ""
    away_team_name = ""
    final_home_url = ""
    final_away_url = ""
    basic_url = "https://understat.com/team/"

    def __init__(self, number_of_matches, home_team_name, away_team_name):
        self.number_of_matches = number_of_matches
        self.home_team_name = home_team_name.title()
        self.away_team_name = away_team_name.title()

    def create_home_url(self):
        self.final_home_url = self.basic_url + self.home_team_name

    def create_away_url(self):
        self.final_away_url = self.basic_url + self.away_team_name

    def get_home_stats(self):
        i = 38
        response = requests.get(self.final_home_url)
        soup = bs(response.content, "html.parser")
        #body > div.wrapper > div.page-wrapper > div:nth-child(3) > div > div.calendar.team.simplebar.custom-scroll_container > div.custom-scroll_inner > div > div:nth-child(38)
        while i > (38 - self.number_of_matches):
            element = soup.select("body > div.wrapper > div.page-wrapper > div:nth-child(3) > div > div.calendar.team.simplebar.custom-scroll_container > div.custom-scroll_inner > div > div:nth-child({})".format(i))
            i -= 1

