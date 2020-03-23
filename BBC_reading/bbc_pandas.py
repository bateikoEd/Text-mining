from selenium import webdriver
from openpyxl import Workbook, load_workbook
import pandas as pd

driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

current_url = 'https://www.bbc.com/ukrainian/topics/c4794229-7f87-43ce-ac0a-6cfcd6d3cef2'

file_name = "panddas.xlsx"
# workbook = load_workbook(filename=name_file)
# workSheet = workbook[sheet_name]
columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

# df_news = pd.DataFrame(columns=columns_my)
df_news = pd.read_excel(file_name, index_col=0)
print(df_news)
# ------- end work with table -------
# enter to new
driver.get(current_url)

main_topics = driver.find_element_by_class_name("page-title").text

list_of_news_of_Ukraine = driver.find_elements_by_xpath('//div[@class="eagle"]/div')
len_of_news = len(list_of_news_of_Ukraine)

for i in range(0, len_of_news):

    driver.get(current_url)
    current_web_elem = driver.find_elements_by_xpath('//div[@class="eagle"]/div')[i]

    current_web_elem.click()

    date = driver.find_element_by_xpath('//li[@class="mini-info-list__item"]/div').text

    topic = driver.find_element_by_tag_name('h1').text
    try:
        author = driver.find_element_by_class_name('byline__name').text
    except:
        author = ''

    text_all_webElem = driver.find_elements_by_class_name("story-body__inner")

    all_text = ''
    for count_paragraph, paragraph in enumerate(text_all_webElem):
        try:
            text_paragraph = paragraph.text + '\n'
            all_text += text_paragraph
            count_paragraph += 1
        except:
            continue

    row = [date, author, main_topics, topic, all_text]
    df_current = pd.DataFrame([row],columns=columns_my)

    df_news = df_news.append(df_current, ignore_index=True)
    print(f"current_df\n:{df_current}")

print(f"df:\n{df_news}")

df_news.to_excel(file_name)
driver.quit()
