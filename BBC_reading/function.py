import datetime
import pandas as pd
import re


def go_to_txt(file_name):
    parameter = ''

    if file_name == 'zn_ua_scraping.xlsx':
        parameter = 'zn_'
    elif file_name == 'bbc_scraping.xlsx':
        parameter = 'bbc_'

    file_name = f"exel_files/{file_name}"
    df_news = pd.read_excel(file_name, index_col=0)

    for i in range(0, len(df_news)):
        file = open(f"bbc/{df_news.iat[i, 2]}/{parameter}{i}.txt", "w+")
        file.write(str(df_news.iat[i, 4]))

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
        date = list_of_message[0]
        current_month = list_of_message[1].strip().lower()
        for month in date_dictionary.keys():
            if current_month.startswith(month):
                return f"{date}/{date_dictionary[month]}/{str(datetime.date.today().year)}"
    except:
        return datetime.date.today().strftime("%d/%m/%Y")

def for_date_nz(date):
    date = re.sub(r', \d{2}:\d{2}','', date)
    date = go_date_bbc(date)
    return date

