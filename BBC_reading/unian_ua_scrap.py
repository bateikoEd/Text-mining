from selenium import webdriver
import time

import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from function import go_date_bbc

def for_date_unian(date):
    date.replace(r', \d{2}:\d{2}', '')
    date = go_date_bbc(date)
    return date

driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

file_name = 'p'
columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

# df_news = pd.read_excel(file_name, index_col=0)

main_url = 'https://dt.ua/POLITICS'

driver.get(main_url)

button_more_news = driver.find_element_by_class_name('more')

list_of_news = driver.find_elements_by_xpath('//li[@class="column x1x2"]/ul/li')

current_new = list_of_news[0]

current_new.click()

topic = driver.find_element_by_class_name('title').text.split()

date = driver.find_element_by_class_name('date').text

date = for_date_unian(date)

text_list = driver.find_elements_by_tag_name('p')

all_text = ""

for elem in text_list:
    try:
        all_text += elem.text + "\n"
    except:
        continue

print(f"title:\t{topic}\ndate:\t{date}\ntext:\n\n{all_text}")

row = [date, '', main_topics_text, topic, all_text]

driver.close()