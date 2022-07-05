class MatchStatusStructure:
    
    def get_stats(self, arr):
        match = {
            "home team": arr[0],
            "away team": arr[1],
            "home score": arr[2],
            "away score": arr[3],
        }
        return match


time = MatchStatusStructure()

time.get_stats(["ciao", "zio"])
