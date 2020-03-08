import pandas as pd
import re
import numpy as np

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)

res_08_03_1 = df.str.extractall(r'(\d{1,2}[/]\d{1,2}[/]\d{2,4})|(\d{1,2}[/]\d{2,4})|(\d{1,2}[-./ ][January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]+[-./, ]+\d{2,4})|([January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]\S+[., -]+\d{2,4}[,. -]+\d{4})|([January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]+\s+\w+[,.]\s+\d{4})')
# print(res_08_03_1.head(100))

#firs column convert to dateTime and addition in date_list
'''count_error = 0
date_list = []
for i in range(0,len(res_08_03_1[0])):
    if res_08_03_1[0].isnull()[2][0] == np.False_ : # no null
        print(i)
        try:
            # print(f"value:\t{res_08_03_1[0][i][0]}\tlen:\t{len(res_08_03_1[0][i][0])}")
            year = res_08_03_1[0][i][0]

            if 8 >= len(year) > 4:
                month = re.search(r'/\d{1,2}/', res_08_03_1[0][i][0][:])
                year = res_08_03_1[0][i][0][:-2] + '19' + res_08_03_1[0][i][0][-2:]

                month = re.search(r'/\d{1,2}/', res_08_03_1[0][i][0])

                if pd.to_numeric(month.group()[1:-1]) <= 12:
                    date_list.append(pd.to_datetime(pd.Series(year), format="%d/%m/%Y"))
                else:
                    date_list.append(pd.to_datetime(pd.Series(year), format="%m/%d/%Y"))
            # print(f"old_year:\t{res_08_03_1[0][i][0]}\tnew_year:\t{year}")
        except TypeError:
            count_error += 1
            continue
        i += 1

print(f"count_error:\t{count_error}")
print(f"date:\t{len(date_list)}")'''

#second column
print(res_08_03_1[1])