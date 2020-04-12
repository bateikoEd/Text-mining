import pandas as pd

file_name="bbc_scraping.xlsx"
file_name = f"exсel_files/{file_name}"

df_news = pd.read_excel(file_name, index_col=0)

print(f"before:\t{len(df_news)}")

df_news.drop_duplicates(inplace=True)

print(f"after:\t{len(df_news)}")

# file_name = "exсel_files/zn_ua_scraping_2.xlsx"
# df_news.to_excel(file_name)