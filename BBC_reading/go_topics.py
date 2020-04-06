from selenium import webdriver
import pandas as pd

from function import go_date_bbc


file_name = "exel_files/zn_ua_scraping.xlsx"
file_name_1 = "exel_files/bbc_scraping.xlsx"
columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

df_news = pd.read_excel(file_name, index_col=0)
print(f"before:\n{df_news.head}")
for coutn, message in enumerate(df_news[columns_my[0]]):

    df_news[columns_my[0]][coutn] = go_date_bbc(message)
    print(f"message:\t{message}\tresult:\t{df_news[columns_my[0]][coutn]}")

print(f"after:\n{df_news.head}")
df_news.to_excel(file_name_1)
