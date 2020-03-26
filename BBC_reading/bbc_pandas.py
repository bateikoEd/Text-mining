from selenium import webdriver
import pandas as pd
import datetime

def go_date_bbc(message):
    date_dictionary = {
        "січ" : "01",
        "лют": "02",
        "берез": "03",
        "квіт": "04",
        "трав": "05",
        "черв": "06",
        "лип": "07",
        "серп": "08",
        "вер": "09",
        "жовт": "10",
        "лист": "11",
        "груд": "12"
    }
    list_of_message = message.split()

    try:
        year = int(list_of_message[2].strip())
        date =  list_of_message[0]
        current_month = list_of_message[1].strip().lower()
        for month in date_dictionary.keys():
            if current_month.startswith(month):
                return f"{date}/{date_dictionary[month]}/{str(datetime.date.today().year)}"
    except:
        return datetime.date.today().strftime("%d/%m/%Y")

driver = webdriver.Chrome(executable_path='/home/bateiko/Downloads/chromedriver_linux64/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()

main_url = 'https://www.bbc.com/ukrainian/topics/ee8750ed-a7fb-453f-bfca-2aa8b3fb064c'

file_name = "panddas1.xlsx"
columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

df_news = pd.read_excel(file_name, index_col=0)

# open browser with first page
driver.get(main_url)

for count_of_main_topics in range(0,7):

    # find maint topics
    count_of_number_one_topic = 2
    count_of_last_topic = 10
    main_topics = driver.find_elements_by_xpath('//div[@class="navigation navigation--wide"]/ul/li')[count_of_number_one_topic:count_of_last_topic]

    # click on main topic
    main_topics[count_of_main_topics].click()
    # update current url
    current_url = driver.current_url

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

        date = driver.find_element_by_xpath('//li[@class="mini-info-list__item"]/div').text
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
        df_current_topic = pd.DataFrame([row],columns=columns_my)
        # addition current new to new's current block
        df_current_block_topics = df_current_block_topics.append(df_current_topic, ignore_index=True)

    # addition new block with news to main new's table
    df_news = df_news.append(df_current_block_topics, ignore_index=True)
    # save in exel +1 block of news
    df_news.to_excel(file_name)

driver.quit()
