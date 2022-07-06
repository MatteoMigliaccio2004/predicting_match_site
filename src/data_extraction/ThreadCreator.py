import threading
import sys
sys.path.append("/src")
from MatchResearcher import MatchResearcher

class myThread(threading.Thread):
    def __init__(self, home_or_away, team_name, number_of_matches):
        threading.Thread.__init__(self)
        self.threadID = home_or_away
        self.name = team_name
        self.counter = number_of_matches
        
    def run(self):
        print("starting {} thread\n".format(self.threadID))
        match_researcher = MatchResearcher(self.counter, self.name)
        stats_list = match_researcher.data_extracter_application()
        i = 0
        while i in  range(len(stats_list)): 
            print(stats_list[i].get_match())
            i += 1
        
if __name__ == "__main__":
    thread1 = (myThread("home", "Inter", 2))
    thread1.start()
    thread2 = (myThread("away", "Cagliari", 2))
    thread2.start()