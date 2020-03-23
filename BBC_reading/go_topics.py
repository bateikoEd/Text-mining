from selenium import webdriver
import pandas as pd

# driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# main_url = 'https://www.bbc.com/ukrainian/news-51018902'
#
# driver.get(main_url)
# date = driver.find_element_by_xpath('//li[@class="mini-info-list__item"]/div').text
#
# print(f"date:\t{date}")

t = True
f = False

if f:
    print(f"1:\t{t}")
elif t:
    print(f"2:\t{f}")
