from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class MainTest():

    def __init__(self):
        options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def main_method(self):
        self.driver.get("https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films")
        site_title = ""

        phase1 = []
        phase2 = []
        phase3 = []

        actions = ActionChains(self.driver)
        """
        1.Complete the following code to find the title of website and store it in site_title.
        2.Complete the following code to get list of first five movies from marvel phase 1 store it in variable phase1.
        3.Complete the following code to get list of first five movies from marvel phase 2 store it in variable phase2.
        1.Complete the following code to get list of directors from first five movies of phase 3,  store it in variable phase3

        """
        # 1.Complete the following code to find the title of website and store it in site_title.
        site_title = self.driver.title

        # 2.Complete the following code to get list of first five movies from marvel phase 1 store it in variable phase1.
        phase1_element = self.driver.find_element(By.XPATH, "(//th/a[text()='Phase One'])[1]")
        actions.move_to_element(phase1_element).perform()

        movies = self.driver.find_elements(By.XPATH, "(//tbody)[2]/tr/th[@scope='row']/i/a")
        for movie in range(5):
            phase1.append(movies[movie].text)

        # 3.Complete the following code to get list of first five movies from marvel phase 2 store it in variable phase2.
        phase2_element = self.driver.find_element(By.XPATH, "(//th/a[text()='Phase Two'])[1]")
        actions.move_to_element(phase2_element).perform()
        for movie in range(6, (6 + 5)):
            phase2.append(movies[movie].text)

        #  4.Complete the following code to get list of directors from first five movies of phase 3,  store it in variable phase3
        phase3_element = self.driver.find_element(By.XPATH, "(//th/a[text()='Phase Three'])[1]")
        actions.move_to_element(phase3_element).perform()
        directors = self.driver.find_elements(By.XPATH, "(//tbody)[2]/tr/td[2]/a")
        for director in range(11, (11 + 5)):
            phase3.append(directors[director].text)

        data = {
            "site_title": site_title,
            "phase1": phase1,
            "phase2": phase2,
            "phase3": phase3

        }
        return data

if __name__ == "__main__":
    test = MainTest()
    print(test.main_method())




