import pandas as pd



def go_to_txt(file_name):

     parameter = ''

     if file_name == 'zn_ua_scraping.xlsx':
          parameter = 'zn_'
     elif file_name == 'bbc_scraping.xlsx':
          parameter = 'bbc_'

     file_name = f"exel_files/{file_name}"
     df_news = pd.read_excel(file_name, index_col=0)


     for i in range(0, len(df_news)):
          file = open(f"bbc/{df_news.iat[i,2]}/{parameter}{i}.txt", "w+")
          file.write(str(df_news.iat[i,4]))

file_name1 = "bbc_scraping.xlsx"
file_name2 = 'zn_ua_scraping.xlsx'

go_to_txt(file_name1)
go_to_txt(file_name2)