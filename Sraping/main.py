import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

main_url = 'https://makeup.com.ua/ua/product/310841/'

driver.get(main_url)

name = driver.find_elemt