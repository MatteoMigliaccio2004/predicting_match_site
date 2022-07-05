class MatchStatusStructure:
    
    match = {} 
    def __init__(self, arr):
        self.match = {
            "home team": arr[0],
            "away team": arr[1],
            "home score": arr[4],
            "away score": arr[5],
            "home shots": arr[8],
            "away shots": arr[9],
            "home target shots": arr[10],
            "away target shots": arr[11],
        }
    
    def get_match(self):
        return self.match
