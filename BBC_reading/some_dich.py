from function import *
from selenium import webdriver
import pandas as pd
import time
import re
import datetime

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
date = '30 березня, 16:49'

print(f"date_before:\t{date}")
# date = re.sub(r', \d{2}:\d{2}','', date)
# date = date.rstrip()
# date = date.replace(r', \d{2}:\d{2}','')
date = for_date_nz(date)

print(f"after:\t{date}")
