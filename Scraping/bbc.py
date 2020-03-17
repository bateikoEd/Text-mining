from selenium import webdriver
from openpyxl import Workbook, load_workbook

driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.bbc.com/ukrainian/topics/c4794229-7f87-43ce-ac0a-6cfcd6d3cef2")

list_of_news_of_Ukraine = driver.find_elements_by_xpath('//div[@class="eagle"]/div')
list_of_information_news = []

for elem in list_of_news_of_Ukraine:
    print(f"tag:\t{elem.tag_name}")


list_of_news_of_Ukraine[0].click()

date_web_element = driver.find_element_by_xpath('//li[@class="mini-info-list__item"]/div')

date = date_web_element.text

paragraphs_in_page = driver.find_elements_by_tag_name('p')
all_text = ''
for paragraph in paragraphs_in_page:
    text_paragraph = paragraph.text + '\n'
    all_text += text_paragraph

print(all_text)



driver.quit()