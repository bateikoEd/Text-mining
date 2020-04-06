import datetime
import pandas as pd
import re



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

# def go_date_nz(message):
#     date_dictionary = {
#         "січ": "01",
#         "лют": "02",
#         "берез": "03",
#         "квіт": "04",
#         "трав": "05",
#         "черв": "06",
#         "лип": "07",
#         "серп": "08",
#         "вер": "09",
#         "жовт": "10",
#         "лист": "11",
#         "груд": "12"
#     }
#     list_of_message = message.split()
#
#     try:
#         year = int(list_of_message[2].strip())
#         date = list_of_message[0]
#         current_month = list_of_message[1].strip().lower()
#         for month in date_dictionary.keys():
#             if current_month.startswith(month):
#                 return f"{date}/{date_dictionary[month]}/{str(datetime.date.today().year)}"
#     except:
#         return datetime.date.today().strftime("%d/%m/%Y")
# def if_exist_in_excel(date, topic, df_news, df_current_block_topics):
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
#
#     columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]
#     df_current_topic = pd.DataFrame([row], columns=columns_my)
#     return df_current_block_topics.append(df_current_topic, ignore_index=True)
#
# def click_on_more_n(driver_1, n=100):
#
#     for count in range(0,n):
#         button_more_news = driver_1.find_elements_by_xpath('//a[@href="javascript:void(0)"]')
#         len_of = len(button_more_news)
#
#         if len_of == 0:
#             return False, len_of
#
#         button_more_new = button_more_news[count]
#         button_more_new.click()
#
#     return True