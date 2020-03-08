from selenium import webdriver
from openpyxl import Workbook, load_workbook

driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.bbc.com/ukrainian/topics/ee8750ed-a7fb-453f-bfca-2aa8b3fb064c")

list_of_news_of_Ukraine = driver.find_elements_by_class_name("eagle")
list_of_information_news = []
for elem_of_news in list_of_news_of_Ukraine:
    elem_title = ''
    elem_date = ''




    elem_information = {'title': elem_of_news.find_element_by_class_name("title-link__title").text,
                        'time': elem_of_news.find_element_by_class_name("date date--v2").text}
    list_of_information_news.append(elem_information)

print(list_of_information_news)