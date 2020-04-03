
from function import go_date_bbc

text = '3 квітня, 01:45'
text.replace(r', \d{2}:\d{2}', '')
text = go_date_bbc(text)

print(text)