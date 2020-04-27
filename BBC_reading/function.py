import datetime
import pandas as pd
import re

def create_all_text(text_list):
    all_text = ""

    for elem in text_list:
        try:
            all_text += elem.text + "\n"
        except:
            continue

    return all_text


def go_to_txt_categorization(file_name):
    parameter = ''

    name_file = {
        'Економіка': 'Economic',
        "Здоров'я": 'Health',
        'Коронавірус': 'Coronavirus',
        'Наука': 'Science',
        'Політика': 'Politic',
        'Спорт': 'Sport',
        'Суспільство': 'Society',
        'Технології': 'Technology',
        'Україна': 'Ukraine'
    }

    if file_name == 'zn_ua_scraping.xlsx':
        parameter = 'zn_'
    elif file_name == 'bbc_scraping.xlsx':
        parameter = 'bbc_'

    file_name = f"exсel_files/{file_name}"
    df_news = pd.read_excel(file_name, index_col=0)

    for i in range(0, len(df_news)):
        directory_name = name_file[df_news.iat[i, 2]]

        file = open(f"Texts/{directory_name}/{parameter}{i}.txt", "w+")
        text = str(df_news.iat[i, 4])
        file.write(text)

def go_to_txt_one_directory(file_name):
    parameter = ''

    if file_name == 'zn_ua_scraping.xlsx':
        parameter = 'zn_'
    elif file_name == 'bbc_scraping.xlsx':
        parameter = 'bbc_'

    file_name = f"exсel_files/{file_name}"
    df_news = pd.read_excel(file_name, index_col=0)

    for i in range(0, len(df_news)):

        file = open(f"all_texts/{parameter}{i}.txt", "w+")
        text = str(df_news.iat[i, 4])
        file.write(text)



def go_date_bbc(message):
    date_dictionary = {
        "січ": "01",
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
        date = int(list_of_message[0])
        current_month = list_of_message[1].strip().lower()
        for month in date_dictionary.keys():
            if current_month.startswith(month):
                return f"{date}/{date_dictionary[month]}/{str(datetime.date.today().year)}"
    except:
        return datetime.date.today().strftime("%d/%m/%Y")


def for_date_nz(date):
    date = re.sub(r', \d{2}:\d{2}', '', date)
    date = go_date_bbc(date)
    return date



