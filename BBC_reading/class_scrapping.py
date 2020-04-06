from selenium import webdriver
import pandas as pd

class Scrapping():
    def __init__(self, ):
        self.driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()