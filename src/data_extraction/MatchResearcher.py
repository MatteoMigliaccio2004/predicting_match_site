import sys
sys.path.append("/src")
from DataExtracter import DataExtracter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MatchResearcher:

    basic_url = "https://understat.com/team/"

    number_of_matches = 0
    team_name = ""
    final_url = ""
    
    def __init__(self, number_of_matches, team_name):
        self.number_of_matches = number_of_matches
        self.team_name = team_name
        

    def get_final_url(self):
        self.final_url = self.basic_url + self.team_name
        return self.final_url

    def get_stats(self):
        
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        wait = WebDriverWait(driver, 10)
        visible = EC.visibility_of_element_located
        
        driver.get(self.get_final_url())
        wait.until(visible((By.CSS_SELECTOR, "body > div.wrapper > div.page-wrapper > div:nth-child(3) > div > div.calendar.team.simplebar.custom-scroll_container > div.custom-scroll_inner > div > div:nth-child(38)")))

        i = len(driver.find_elements(By.CLASS_NAME, "calendar-date-container"))
        total_matches = i
        url_list = []
        
        while i > (total_matches - self.number_of_matches):
            value = driver.find_element(By.CSS_SELECTOR, "body > div.wrapper > div.page-wrapper > div:nth-child(3) > div > div.calendar.team.simplebar.custom-scroll_container > div.custom-scroll_inner > div > div:nth-child({}) > div.calendar-games > div > a".format(i)).get_attribute("href")
            url_list.append(value)
            i -= 1
            
        return url_list
    
    def data_extracter_application(self):
        i = 0
        url_list = self.get_stats()
        matches_stats = []
        
        while i < self.number_of_matches:
            data_extracter = DataExtracter(url_list[i])
            matches_stats.append(data_extracter.get_structure())
            i += 1
            
        return matches_stats