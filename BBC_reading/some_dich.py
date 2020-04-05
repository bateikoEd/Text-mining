from function import *
from selenium import webdriver
import pandas as pd

file_name="exel_files/zn_ua_scraping.xlsx"

current_url = 'https://dt.ua/POLITICS/postpred-ukrayini-v-oon-rozpoviv-yak-rosiya-peretvoryuye-koronavirus-na-politichnu-zbroyu-343678_.html'
main_topics_text = 'Політика'

columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get(current_url)


topic = driver.find_element_by_class_name('title').text.strip()

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

df_news = pd.DataFrame([row], columns=columns_my)
df_news.to_excel(file_name)
driver.close()