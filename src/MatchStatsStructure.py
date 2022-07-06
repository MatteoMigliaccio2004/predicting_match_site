class MatchStatusStructure:
    
    match = {} 
    
    def __init__(self, arr):
        self.match = {
            "home team": arr[0],
            "away team": arr[1],
            "home score": arr[5],
            "away score": arr[6],
            "home shots": arr[9],
            "away shots": arr[10],
            "home target shots": arr[11],
            "away target shots": arr[12],
        }
    
    def get_match(self):
        return self.match
