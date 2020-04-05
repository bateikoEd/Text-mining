from function import *
from selenium import webdriver
import pandas as pd

# def if_exist_in_excel(date, topic):
#     if len(df_news.loc[(df_news['Date'] == date) & (df_news['Topic'] == topic)]) > 0:
#         print("Present")
#         return True
#
#     elif len(df_current_block_topics.loc[
#                  (df_current_block_topics['Date'] == date) & (df_current_block_topics['Topic'] == topic)]) > 0:
#         print("Present")
#         return True
#
#     print("Not present")
#     return False
#
# def create_all_text(text_list):
#     all_text = ""
#
#     for elem in text_list:
#         try:
#             all_text += elem.text + "\n"
#         except:
#             continue
# 
#     return all_text
#
# def add_new_current_block_topic(row, df_current_block_topics):
#     df_current_topic = pd.DataFrame([row], columns=columns_my)
#     return df_current_block_topics.append(df_current_topic, ignore_index=True)
#
# def click_on_more_n(n=100):
#
#     for count in range(0,n):
#         button_more_news = driver.find_elements_by_xpath('//a[@href="javascript:void(0)"]')
#         len_of = len(button_more_news)
#
#         if len_of == 0:
#             return False, len_of
#
#         button_more_new = button_more_news[count]
#         button_more_new.click()
#         # driver.implicitly_wait(3)
#
#     return True


file_name="exel_files/zn_ua_scraping.xlsx"

main_topics_url = ['https://dt.ua/POLITICS',
                       'https://dt.ua/ECONOMICS',
                       'https://dt.ua/TECHNOLOGIES'
                       'https://dt.ua/SPORT',
                       'https://dt.ua/UKRAINE']

main_topics_url_special = ['https://dt.ua/theme/69',
                           'https://dt.ua/theme/74',
                           'https://dt.ua/theme/71']

main_topics_text = ['Політика', 'Економіка','Технології','Спорт','Україна']
driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

main_topics_text = main_topics_text[0]
main_url = main_topics_url[0]

driver.get(main_url)
bool_res, max_count = click_on_more_n()

columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

df_news = pd.read_excel(file_name, index_col=0)

columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

driver.get(main_url)

for count_of_more in range(0, max_count):

    list_of_news = driver.find_elements_by_xpath('//li[@class="column x1x2"]/ul/li')

    len_old_news = 0 if count_of_more == 0 else len_new_news
    len_new_news = len(list_of_news)

    print(f"len_olf:\t{len_old_news}\tlen_new:\t{len_new_news}")

    # --- create block of news ---
    df_current_block_topics = pd.DataFrame(columns=columns_my)

    for count_of_current_news in range(len_old_news, len_new_news):

        driver.get(main_url)
        list_of_news = driver.find_elements_by_xpath('//li[@class="column x1x2"]/ul/li')
        # driver.implicitly_wait(5)
        print(f"coutn:\t{count_of_current_news}")
        current_new = list_of_news[count_of_current_news]
        current_new.click()
        # driver.implicitly_wait(5)

        # ---- start read new ---
        topic = driver.find_element_by_class_name('title').text.strip()

        date = driver.find_element_by_class_name('date').text

        date = for_date_unian(date)

        # condition if we have the current topic with same date
        if if_exist_in_excel(date, topic):
            continue

        text_list = driver.find_elements_by_tag_name('p')

        all_text = create_all_text(text_list)

        # ---- end read new ---
        row = [date, '', main_topics_text, topic, all_text]

        df_current_block_topics = add_new_current_block_topic(row=row, df_current_block_topics=df_current_block_topics)

    df_news = df_news.append(df_current_block_topics, ignore_index=True)


driver.close()