import pandas as pd


file_name = "panddas1.xlsx"
columns_my = ["Date", "Author", "Main_Topics", "Topic", "Text"]

df_news = pd.read_excel(file_name, index_col=0)

for i in range(0, len(df_news)):
     file = open(f"bbc/{df_news.iat[i,2]}/{i}.txt", "w+")
     # file = open(f"{i}.txt", "w+")
     file.write(str(df_news.iat[i,4]))
