from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

main_url = 'https://www.bbc.com/ukrainian/topics/ee8750ed-a7fb-453f-bfca-2aa8b3fb064c'

file_name = "panddas.xlsx"
columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

df_news = pd.read_excel(file_name, index_col=0)

# open browser with first page
driver.get(main_url)

for count_of_main_topics in range(0,7):

    # find
    main_topics = driver.find_elements_by_xpath('//div[@class="navigation navigation--wide"]/ul/li')[2:10]

    # click on main topic
    main_topics[count_of_main_topics].click()

    current_url = driver.current_url

    main_topics = driver.find_element_by_class_name("page-title").text

    print(f"main_topic:\t{main_topics}\tcount:\t{count_of_main_topics}")

    list_of_news_of_Ukraine = driver.find_elements_by_xpath('//div[@class="eagle"]/div')
    len_of_news = len(list_of_news_of_Ukraine)

    df_current_block_topics = pd.DataFrame(columns=columns_my)

    for count_of_topic in range(0, len_of_news):

        driver.get(current_url)
        current_web_elem = driver.find_elements_by_xpath('//div[@class="eagle"]/div')[count_of_topic]

        current_web_elem.click()

        date = driver.find_element_by_xpath('//li[@class="mini-info-list__item"]/div').text
        topic = driver.find_element_by_tag_name('h1').text

        if len(df_news.loc[(df_news['Date'] == date) & (df_news['Topic'] == topic)]) > 0:
            continue
        elif len(df_current_block_topics.loc[(df_current_block_topics['Date'] == date) & (df_current_block_topics['Topic'] == topic)]) > 0:
            continue

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
        df_current_topic = pd.DataFrame([row],columns=columns_my)

        df_current_block_topics = df_current_block_topics.append(df_current_topic, ignore_index=True)

    df_news = df_news.append(df_current_block_topics, ignore_index=True)

    df_news.to_excel(file_name)


print(f"df:\n{df_news}")

driver.quit()
