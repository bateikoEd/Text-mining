from selenium import webdriver
import pandas as pd
import time

from function import for_date_nz, go_date_bbc, go_to_txt, create_all_text


class Scrapping:
    def __init__(self, ):
        self.driver = webdriver.Chrome(executable_path='chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]
        self.df_news = pd.DataFrame([], columns=self.columns_my)
        self.file_names = ['bbc_scraping.xlsx', 'zn_ua_scraping.xlsx']

    def if_exist_in_excel(self, date, topic, df_current_block_topics):
        if len(self.df_news.loc[(self.df_news['Date'] == date) & (self.df_news['Topic'] == topic)]) > 0:
            print("PRESENT")
            return True

        elif len(df_current_block_topics.loc[
                     (df_current_block_topics['Date'] == date) & (df_current_block_topics['Topic'] == topic)]) > 0:
            print("PRESENT")
            return True

        print("NOT PRESENT")
        return False

    def add_new_current_block_topic(self, row, df_current_block_topics):
        df_current_topic = pd.DataFrame([row], columns=self.columns_my)
        return df_current_block_topics.append(df_current_topic, ignore_index=True)

    def click_on_more_n(self, n):
        if n == 0:
            return
        for count in range(0, n):
            button_more_news = self.driver.find_elements_by_link_text('Показати більше статей')
            len_of = len(button_more_news)

            if len_of == 0:
                return
            try:
                button_more_news[0].click()
            except:
                return

        return True

    def close_driver(self):
        self.driver.close()

    def nz_authorization(self):
        login = 'bateiko'
        password = '25896ok@la'

        authorization = self.driver.find_element_by_xpath('//*[@id="header"]/div/a[4]')
        authorization.click()

        login_tag = self.driver.find_element_by_id('passport_name')
        password_tag = self.driver.find_element_by_id('passport_password')

        login_tag.send_keys(login)
        password_tag.send_keys(password)
        password_tag.submit()
        time.sleep(2)

    def to_current_url(self, main_url):
        self.driver.get(main_url)

    '''
        Політика - 0
        Економіка - 1
        Технології - 2
        Спорт - 3
        Україна - 4
        corona in the world - 1.0
        carantin in ukraine - 1.1
        ooc - 1.2'''

    def nz_scrapping(self, main_topics_count_min=0, len_new_news=0, max_count=2, if_topic_present=True,
                     file_name="zn_ua_scraping.xlsx"):
        file_name = f"exсel_files/{file_name}"

        main_topics_url = ['https://dt.ua/POLITICS',
                           'https://dt.ua/ECONOMICS',
                           'https://dt.ua/TECHNOLOGIES',
                           'https://dt.ua/SPORT',
                           'https://dt.ua/UKRAINE']

        main_topics_url_special = ['https://dt.ua/theme/69',
                                   'https://dt.ua/theme/74',
                                   'https://dt.ua/theme/71']
        main_topics_text = ['Політика', 'Економіка', 'Технології', 'Спорт', 'Україна']

        count_of_start = len_new_news // 12 + 1 if len_new_news % 12 != 0 else len_new_news // 12

        main_topic_text = main_topics_text[main_topics_count_min]
        main_url = main_topics_url[main_topics_count_min]

        columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

        self.to_current_url(main_url)
        time.sleep(2)

        self.nz_authorization()

        self.df_news = pd.read_excel(file_name, index_col=0)

        # print(f"head:\n\n{df_news.all}")

        for count_of_topic, main_url in enumerate(main_topics_url[main_topics_count_min:], main_topics_count_min):

            main_topic_text = main_topics_text[count_of_topic]
            print(f"main_topic:\t{main_topic_text}")

            self.to_current_url(main_url)
            time.sleep(3)

            for count_of_more in range(count_of_start, max_count):

                self.click_on_more_n(count_of_more)
                time.sleep(2)

                list_of_news = self.driver.find_elements_by_xpath('//li[@class="column x1x2"]/ul/li')
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

                    self.to_current_url(main_url)
                    time.sleep(4)
                    self.click_on_more_n(count_of_more)
                    time.sleep(1)

                    list_of_news = self.driver.find_elements_by_xpath('//li[@class="column x1x2"]/ul/li')
                    time.sleep(1)

                    len_new_news_current = len(list_of_news)
                    print(f"len_old:\t{len_old_news}\tlen_current:\t{len_new_news_current}")

                    print(f"count:\t{count_of_current_news}")
                    current_new = list_of_news[count_of_current_news]
                    current_new.click()
                    time.sleep(1)

                    # ---- start read new ---
                    topic = self.driver.find_element_by_class_name('title').text.strip()

                    try:
                        date = self.driver.find_element_by_class_name('date').text
                    except:
                        continue

                    date = for_date_nz(date)

                    print(f"Topic:\t{topic}\tdate:\t{date}")

                    # condition if we have the current topic with same date
                    if self.if_exist_in_excel(date, topic, df_current_block_topics):
                        if if_topic_present:
                            break
                        continue

                    text_list = self.driver.find_elements_by_tag_name('p')

                    all_text = create_all_text(text_list)

                    # ---- end read new ---
                    row = [date, '', main_topic_text, topic, all_text]

                    df_current_block_topics = self.add_new_current_block_topic(row=row,
                                                                               df_current_block_topics=df_current_block_topics)

                self.df_news = self.df_news.append(df_current_block_topics, ignore_index=True)
                self.df_news.to_excel(file_name)

    '''
        коронавірус - 0
        Політика - count_of_number_one_topic = 1
        Економіка - 2
        Суспільство - 3
        Наука - 4
        Технології - 5
        Health - 6
        Спорт - 7'''

    def bbc_scraping(self, count_of_number_one_topic=0, count_of_last_topic=8, if_topic_present=True,
                     file_name="bbc_scraping.xlsx"):

        main_topics_url = ['https://www.bbc.com/ukrainian/topics/5fe79b8d-56e5-4aff-8b05-21f9ad731912',
                           'https://www.bbc.com/ukrainian/topics/ca170ae3-99c1-48db-9b67-2866f85e7342',
                           'https://www.bbc.com/ukrainian/topics/5307a8d9-f620-40f5-92d4-f99c919a6ffa',
                           'https://www.bbc.com/ukrainian/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53',
                           'https://www.bbc.com/ukrainian/topics/31684f19-84d6-41f6-b033-7ae08098572a',
                           'https://www.bbc.com/ukrainian/topics/c4794229-7f87-43ce-ac0a-6cfcd6d3cef2',
                           'https://www.bbc.com/ukrainian/topics/4063f80f-cccc-44c8-9449-5ca44e4c8592',
                           'https://www.bbc.com/ukrainian/topics/75612fa6-147c-4a43-97fa-fcf70d9cced3']

        file_name = f"exсel_files/{file_name}"

        main_url = main_topics_url[0]

        self.df_news = pd.read_excel(file_name, index_col=0)

        for count_of_main_topics, current_url in enumerate(
                main_topics_url[count_of_number_one_topic:count_of_last_topic]):

            self.to_current_url(current_url)

            main_topics_text = self.driver.find_element_by_class_name("page-title").text

            print(f"main_topic:\t{main_topics_text}\tcount:\t{count_of_main_topics}")

            # list of news in current block
            list_of_news_of_Ukraine = self.driver.find_elements_by_xpath('//div[@class="eagle"]/div')
            len_of_news = len(list_of_news_of_Ukraine)

            # create dataFrame object for one block for main topic
            df_current_block_topics = pd.DataFrame(columns=self.columns_my)

            for count_of_topic in range(0, len_of_news):
                # update webpage
                self.to_current_url(current_url)
                current_web_elem = self.driver.find_elements_by_xpath('//div[@class="eagle"]/div')[count_of_topic]

                # click on current new
                current_web_elem.click()

                try:
                    date = self.driver.find_element_by_xpath('//li[@class="mini-info-list__item"]/div').text
                except:
                    date = self.driver.find_element_by_xpath('//*[@id="root"]/main/div[3]/time').text
                topic = self.driver.find_element_by_tag_name('h1').text

                date = go_date_bbc(date)

                print(f"Topic:\t{topic}\tdate:\t{date}")

                # condition if we have the current topic with same date
                if self.if_exist_in_excel(date, topic, df_current_block_topics):
                    if if_topic_present:
                        break
                    continue

                try:
                    author = self.driver.find_element_by_class_name('byline__name').text
                except:
                    author = ''

                text_all_webElem = self.driver.find_elements_by_class_name("story-body__inner")

                all_text = create_all_text(text_all_webElem)

                row = [date, author, main_topics_text, topic, all_text]
                df_current_block_topics = self.add_new_current_block_topic(row=row,
                                                                           df_current_block_topics=df_current_block_topics)

            # addition new block with news to main new's table
            self.df_news = self.df_news.append(df_current_block_topics, ignore_index=True)
            # save in exel +1 block of news
            self.df_news.to_excel(file_name)

    def to_all_txt(self):
        for elem in self.file_names:
            go_to_txt(file_name=elem)

    def len_of_news(self):
        file_name = self.file_names[0]
        file_name = f"exсel_files/{file_name}"

        self.df_news = pd.read_excel(file_name, index_col=0)
        bbc_len = len(self.df_news)

        file_name = self.file_names[1]
        file_name = f"exсel_files/{file_name}"

        self.df_news = pd.read_excel(file_name, index_col=0)
        nz_len = len(self.df_news)

        all_len = nz_len + bbc_len
        print(f"bbc_len:\t{bbc_len}\tnz_len:\t{nz_len}\nall_len:\t{all_len}")

    # def __del__(self):
    #     self.driver.quit()
