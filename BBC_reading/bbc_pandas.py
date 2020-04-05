from selenium import webdriver
import pandas as pd

from function import go_date_bbc, for_date_unian

'''
    коронавірус - 0
    Політика - count_of_number_one_topic = 1
    Економіка - 2
    Суспільство - 3
    Наука - 4
    Технології - 5
    Здоров'я - 6
    Спорт - 7
    Україна - count_of_number_one_topic = 8'''
def bbc_scraping(count_of_number_one_topic=0, count_of_last_topic=8, file_name="bbc_scraping.xlsx"):

    main_topics_url = ['https://www.bbc.com/ukrainian/topics/5fe79b8d-56e5-4aff-8b05-21f9ad731912',
                       'https://www.bbc.com/ukrainian/topics/ca170ae3-99c1-48db-9b67-2866f85e7342',
                       'https://www.bbc.com/ukrainian/topics/5307a8d9-f620-40f5-92d4-f99c919a6ffa',
                       'https://www.bbc.com/ukrainian/topics/0f469e6a-d4a6-46f2-b727-2bd039cb6b53',
                       'https://www.bbc.com/ukrainian/topics/31684f19-84d6-41f6-b033-7ae08098572a',
                       'https://www.bbc.com/ukrainian/topics/c4794229-7f87-43ce-ac0a-6cfcd6d3cef2',
                       'https://www.bbc.com/ukrainian/topics/4063f80f-cccc-44c8-9449-5ca44e4c8592',
                        'https://www.bbc.com/ukrainian/topics/75612fa6-147c-4a43-97fa-fcf70d9cced3']

    file_name = f"exel_files/{file_name}"
    driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
    driver.implicitly_wait(5)
    driver.maximize_window()

    main_url = main_topics_url[0]

    columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

    df_news = pd.read_excel(file_name, index_col=0)

    for count_of_main_topics, current_url in enumerate(main_topics_url[count_of_number_one_topic:count_of_last_topic]):

        driver.get(current_url)

        main_topics_text = driver.find_element_by_class_name("page-title").text

        print(f"main_topic:\t{main_topics_text}\tcount:\t{count_of_main_topics}")

        # list of news in current block
        list_of_news_of_Ukraine = driver.find_elements_by_xpath('//div[@class="eagle"]/div')
        len_of_news = len(list_of_news_of_Ukraine)

        # create dataFrame object for one block for main topic
        df_current_block_topics = pd.DataFrame(columns=columns_my)

        for count_of_topic in range(0, len_of_news):
            # update webpage
            driver.get(current_url)
            current_web_elem = driver.find_elements_by_xpath('//div[@class="eagle"]/div')[count_of_topic]

            # click on current new
            current_web_elem.click()

            try:
                date = driver.find_element_by_xpath('//li[@class="mini-info-list__item"]/div').text
            except:
                date = driver.find_element_by_xpath('//*[@id="root"]/main/div[3]/time').text
            topic = driver.find_element_by_tag_name('h1').text

            date = go_date_bbc(date)

            print(f"Topic:\t{topic}\tdate:\t{date}")

            # condition if we have the current topic with same date
            if len(df_news.loc[(df_news['Date'] == date) & (df_news['Topic'] == topic)]) > 0:
                print("Present")
                continue
            elif len(df_current_block_topics.loc[(df_current_block_topics['Date'] == date) & (df_current_block_topics['Topic'] == topic)]) > 0:
                print("Present")
                continue
            print("Not present")
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


            row = [date, author, main_topics_text, topic, all_text]
            df_current_topic = pd.DataFrame([row], columns=columns_my)
            # addition current new to new's current block
            df_current_block_topics = df_current_block_topics.append(df_current_topic, ignore_index=True)

        # addition new block with news to main new's table
        df_news = df_news.append(df_current_block_topics, ignore_index=True)
        # save in exel +1 block of news
        df_news.to_excel(file_name)

    driver.quit()
    
'''
    Політика - 0
    Економіка - 1
    Технології - 2
    Спорт - 3
    Україна - 4
    corona in the world - 1.0
    carantin in ukraine - 1.1
    ooc - 1.2'''
def zn_scraping(count_of_number_one_topic=0, count_of_last_topic=8, file_name="bbc_scraping.xlsx"):

    main_topics_url = ['https://dt.ua/POLITICS',
                       'https://dt.ua/ECONOMICS',
                       'https://dt.ua/TECHNOLOGIES'
                       'https://dt.ua/SPORT',
                       'https://dt.ua/UKRAINE']

    main_topics_url_special = ['https://dt.ua/theme/69',
                               'https://dt.ua/theme/74',
                               'https://dt.ua/theme/71']
    main_topics_text = ['Політика', 'Економіка','Україна','Технології','Спорт']
    driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
    driver.implicitly_wait(5)
    driver.maximize_window()

    main_topics_text = main_topics_text[0]
    main_url = main_topics_url[0]

    columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

    df_news = pd.read_excel(file_name, index_col=0)

    file_name = 'p'
    columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

    # df_news = pd.read_excel(file_name, index_col=0)

    main_url = 'https://dt.ua/POLITICS'

    driver.get(main_url)

    button_more_news = driver.find_element_by_class_name('more')

    list_of_news = driver.find_elements_by_xpath('//li[@class="column x1x2"]/ul/li')

    current_new = list_of_news[0]

    current_new.click()

    topic = driver.find_element_by_class_name('title').text.split()

    date = driver.find_element_by_class_name('date').text

    date = for_date_unian(date)

    text_list = driver.find_elements_by_tag_name('p')

    all_text = ""

    for elem in text_list:
        try:
            all_text += elem.text + "\n"
        except:
            continue

    print(f"title:\t{topic}\ndate:\t{date}\ntext:\n\n{all_text}")

    row = [date, '', main_topics_text, topic, all_text]
    df_current_topic = pd.DataFrame([row], columns=columns_my)
    # addition current new to new's current block
    df_current_block_topics = df_current_block_topics.append(df_current_topic, ignore_index=True)

    driver.close()



