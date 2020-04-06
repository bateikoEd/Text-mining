from function import *
from selenium import webdriver
import pandas as pd
import time
import re
import datetime



# login = 'bateiko'
# password = '25896ok@la'
#
# main_url = 'https://dt.ua/POLITICS/verhovna-rada-progolosuvala-za-priznachennya-stepanova-novim-glavoyu-moz-343057_.html'
#
# driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.get(main_url)
#
# authorization = driver.find_element_by_xpath('//*[@id="header"]/div/a[4]')
# authorization.click()
#
# login_tag = driver.find_element_by_id('passport_name')
# password_tag = driver.find_element_by_id('passport_password')
#
# login_tag.send_keys(login)
# password_tag.send_keys(password)
# password_tag.submit()
#
# time.sleep(5)
#
# date = driver.find_element_by_class_name('date').text


file_name= "exel_files/zn_ua_scraping.xlsx"
df_news = pd.read_excel(file_name, index_col=0)
print(df_news.head)