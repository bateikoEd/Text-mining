from selenium import webdriver
import pandas as pd

from function import go_date_bbc


driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

file_name = 'p'
columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

df_news = pd.read_excel(file_name, index_col=0)

main_url = 'https://dt.ua/POLITICS'

list_of_news = driver.find_elements_by_xpath('//ul[@class="index_news_list"]//li[@class="column x1x2"]/ul/li')

button_more_news = driver.find_element_by_class_name('more')