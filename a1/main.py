import pandas as pd
import re
import numpy as np
import calendar as cal
from datetime import datetime


def define_number_of_month(name_month):
    month_name_number = {}
    for x in range(1, 13):
        month_name_number[cal.month_name[x].lower()] = x
        month_name_number[cal.month_abbr[x].lower()] = x

    try:
        return month_name_number[name_month.lower()]
    except KeyError:
        return None


doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)

res_08_03_1 = df.str.extractall(
    r'(\d{1,2}[/]\d{1,2}[/]\d{2,4})|(\d{1,2}[/]\d{2,4})|(\d{1,2}[-./ ][January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]+[-./, ]+\d{2,4})|([January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]\S+[., -]+\d{2,4}[,. -]+\d{4})|([January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]+\s+\w+[,.]\s+\d{4})')

# firs column convert to dateTime and addition in date_list
date_list = []

# date_list = pd.Series([], dtype=type(pd.DateTime))
for i in range(0, pd.to_numeric(res_08_03_1.index[-1][0])):
    try:
        if res_08_03_1[0].isnull()[i][0] == np.False_:
            year = res_08_03_1[0][i][0]

            if 8 >= len(year) > 4:
                year = '19' + res_08_03_1[0][i][0][-2:]

                month = re.search(r'/\d{1,2}/', res_08_03_1[0][i][0])

                date = res_08_03_1[0][i][0][:-2] + year

                if pd.to_numeric(month.group()[1:-1]) > 12:
                    day = re.search(r'\d{1,2}/', res_08_03_1[0][i][0])
                    date = f"{month.group()[1:-1]}/{day.group()[:-1]}/{year}"

                date_list.append(pd.to_datetime(date, format="%d/%m/%Y"))

    except TypeError:
        continue

    except IndexError:
        continue

# second column convert to dateTime and addition in date_list
for i in range(0, pd.to_numeric(res_08_03_1.index[-1][0])):
    try:
        if res_08_03_1[1].isnull()[i][0] == np.False_:
            date = res_08_03_1[1][i][0]

            if 8 >= len(date) >= 4:

                date = '1/' + date
                date_list.append(pd.to_datetime(date, format="%d/%m/%Y"))
    except TypeError:
        continue

    except IndexError:
        continue

# third column
for i in range(0, pd.to_numeric(res_08_03_1.index[-1][0])):
    try:
        if res_08_03_1[2].isnull()[i][0] == np.False_:
            date = res_08_03_1[2][i][0]

            name_month = re.search(r' \w{3,9} ', date)

            if name_month is not None:
                date = f"{date[:2]}/{define_number_of_month(name_month.group().strip())}/{date[-4:]}"
                date_list.append(pd.to_datetime(date, format="%d/%m/%Y"))
    except TypeError:
        continue

    except IndexError:
        continue


#forth column
for i in range(0, pd.to_numeric(res_08_03_1.index[-1][0])):
    try:
        if res_08_03_1[3].isnull()[i][0] == np.False_:
            date = res_08_03_1[3][i][0]
            day = re.search(r' \d{2}[ .,]', date)
            month = re.search(r'\w{3,9}', date)
            year = re.search(r'\d{4}', date)

            day = day.group()[1:-1]
            month = define_number_of_month(month.group())
            year = year.group()

            date = f"{day}/{month}/{year}"
            date_list.append(pd.to_datetime(date, format="%d/%m/%Y"))
    #            date_list.append(pd.to_datetime(pd.Series(date), format="%d/%m/%Y"))

    except IndexError:
        continue

    except ValueError:
        continue

#convert to Series
new_series = pd.Series(date_list)
#sorting
print(new_series.argsort())

