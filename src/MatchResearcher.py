import sys
sys.path.append("/src")
from DataExtracter import DataExtracter

class MatchResearcher:

    number_of_matches = 0

    def __init__(self, number):
        self.number_of_matches = number
