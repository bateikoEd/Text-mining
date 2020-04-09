from function import *
from selenium import webdriver
import pandas as pd
import time


def if_exist_in_excel(date, topic):
    if len(df_news.loc[(df_news['Date'] == date) & (df_news['Topic'] == topic)]) > 0:
        print("Present")
        return True

    elif len(df_current_block_topics.loc[
                 (df_current_block_topics['Date'] == date) & (df_current_block_topics['Topic'] == topic)]) > 0:
        print("Present")
        return True

    print("Not present")
    return False


def create_all_text(text_list):
    all_text = ""

    for elem in text_list:
        try:
            all_text += elem.text + "\n"
        except:
            continue

    return all_text


def add_new_current_block_topic(row, df_current_block_topics):
    df_current_topic = pd.DataFrame([row], columns=columns_my)
    return df_current_block_topics.append(df_current_topic, ignore_index=True)


def click_on_more_n(n):
    if n == 0:
        return
    for count in range(0, n):
        button_more_news = driver.find_elements_by_link_text('Показати більше статей')
        len_of = len(button_more_news)

        if len_of == 0:
            return
        try:
            button_more_news[0].click()
        except:
            return

    return True


file_name = "exel_files/zn_ua_scraping.xlsx"

main_topics_url = ['https://dt.ua/POLITICS',
                   'https://dt.ua/ECONOMICS',
                   'https://dt.ua/TECHNOLOGIES',
                   'https://dt.ua/SPORT',
                   'https://dt.ua/UKRAINE']

main_topics_url_special = ['https://dt.ua/theme/69',
                           'https://dt.ua/theme/74',
                           'https://dt.ua/theme/71']

main_topics_text = ['Політика', 'Економіка', 'Технології', 'Спорт', 'Україна']
driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

# ----------------------------
main_topics_count_min = 0
len_new_news = 0

count_of_start = len_new_news // 12 + 1 if len_new_news % 12 != 0 else len_new_news // 12
max_count = 2


main_topic_text = main_topics_text[main_topics_count_min]
main_url = main_topics_url[main_topics_count_min]

columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]
driver.get(main_url)
time.sleep(2)

# --- authorization
login = 'bateiko'
password = '25896ok@la'

authorization = driver.find_element_by_xpath('//*[@id="header"]/div/a[4]')
authorization.click()

login_tag = driver.find_element_by_id('passport_name')
password_tag = driver.find_element_by_id('passport_password')

login_tag.send_keys(login)
password_tag.send_keys(password)
password_tag.submit()
time.sleep(2)

# ----------------

df_news = pd.read_excel(file_name, index_col=0)

for count_of_topic, main_url in enumerate(main_topics_url[main_topics_count_min:], main_topics_count_min):

    main_topic_text = main_topics_text[count_of_topic]
    print(f"main_topic:\t{main_topic_text}")

    driver.get(main_url)
    time.sleep(2)

    for count_of_more in range(count_of_start, max_count):

        click_on_more_n(count_of_more)
        time.sleep(1)

        list_of_news = driver.find_elements_by_xpath('//li[@class="column x1x2"]/ul/li')
        # time.sleep(1)

        len_old_news = len_new_news
        len_new_news = len(list_of_news)

        print(f"len_old:\t{len_old_news}\tlen_new:\t{len_new_news}")

        if len_new_news <= len_old_news:
            print(f"len_new <= len_old")
            len_new_news = 0
            count_of_start = 0
            break

        # --- create block of news ---
        df_current_block_topics = pd.DataFrame(columns=columns_my)

        for count_of_current_news in range(len_old_news, len_new_news):

            driver.get(main_url)
            time.sleep(1)
            click_on_more_n(count_of_more)
            time.sleep(1)

            list_of_news = driver.find_elements_by_xpath('//li[@class="column x1x2"]/ul/li')
            time.sleep(1)

            len_new_news_current = len(list_of_news)
            print(f"len_old:\t{len_old_news}\tlen_current:\t{len_new_news_current}")

            print(f"coutn:\t{count_of_current_news}")
            current_new = list_of_news[count_of_current_news]
            current_new.click()
            time.sleep(1)

            # ---- start read new ---
            topic = driver.find_element_by_class_name('title').text.strip()

            try:
                date = driver.find_element_by_class_name('date').text
            except:
                continue

            date = for_date_nz(date)

            print(f"Topic:\t{topic}\tdate:\t{date}")

            # condition if we have the current topic with same date
            if if_exist_in_excel(date, topic):
                continue

            text_list = driver.find_elements_by_tag_name('p')

            all_text = create_all_text(text_list)

            # ---- end read new ---
            row = [date, '', main_topic_text, topic, all_text]

            df_current_block_topics = add_new_current_block_topic(row=row,
                                                                  df_current_block_topics=df_current_block_topics)

        len_old_news = 0

        df_news = df_news.append(df_current_block_topics, ignore_index=True)
        df_news.to_excel(file_name)

driver.close()
