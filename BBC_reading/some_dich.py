from function import *
from selenium import webdriver
import pandas as pd

def click_on_more_n(n=100):

    for count in range(0,n):
        button_more_news = driver.find_elements_by_xpath('//a[@href="javascript:void(0)"]')
        len_of = len(button_more_news)

        if len_of == 0:
            return False, len_of

        button_more_new = button_more_news[count]
        button_more_new.click()
        # driver.implicitly_wait(3)

    return True

# file_name="exel_files/zn_ua_scraping.xlsx"

# current_url = 'https://dt.ua/POLITICS/postpred-ukrayini-v-oon-rozpoviv-yak-rosiya-peretvoryuye-koronavirus-na-politichnu-zbroyu-343678_.html'
# main_topics_text = 'Політика'

main_url = 'https://dt.ua/ECONOMICS'

driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get(main_url)
driver.implicitly_wait(10)
print(f"eduard")
close_tab = driver.find_elements_by_xpath('//*[@id="simplemodal-container"]/a')
if len(close_tab) > 0:
    close_tab[0].click()

bool_res, max_count = click_on_more_n()

print(f"max:\t{max_count}")