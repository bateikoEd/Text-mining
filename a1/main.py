import pandas as pd
import re
import numpy as np
from time import strptime
import calendar as cal


def define_number_of_month(name_month):
    month_name_number = {}
    for x in range(1, 13):
        month_name_number[cal.month_name[x].lower()] = x
        month_name_number[cal.month_abbr[x].lower()] = x

    return month_name_number[name_month.lower()]


doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)

res_08_03_1 = df.str.extractall(
    r'(\d{1,2}[/]\d{1,2}[/]\d{2,4})|(\d{1,2}[/]\d{2,4})|(\d{1,2}[-./ ][January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]+[-./, ]+\d{2,4})|([January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]\S+[., -]+\d{2,4}[,. -]+\d{4})|([January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]+\s+\w+[,.]\s+\d{4})')
# print(res_08_03_1.head(100))
# pd.to_numeric(res_08_03_1.index[-1][0])

# firs column convert to dateTime and addition in date_list
type_error, index_error, count = 0, 0, 0
date_list = []
for i in range(0, pd.to_numeric(res_08_03_1.index[-1][0])):
    if res_08_03_1[0].isnull()[i][0] == np.False_:  # no null
        try:
            # print(f"value:\t{res_08_03_1[0][i][0]}\tlen:\t{len(res_08_03_1[0][i][0])}")
            year = res_08_03_1[0][i][0]

            if 8 >= len(year) > 4:
                year = res_08_03_1[0][i][0][:-2] + '19' + res_08_03_1[0][i][0][-2:]

                month = re.search(r'/\d{1,2}/', res_08_03_1[0][i][0])

                if pd.to_numeric(month.group()[1:-1]) <= 12:
                    date_list.append(pd.to_datetime(pd.Series(year), format="%d/%m/%Y"))
                else:
                    date_list.append(pd.to_datetime(pd.Series(year), format="%m/%d/%Y"))
            # print(f"old_year:\t{res_08_03_1[0][i][0]}\tnew_year:\t{year}")
        except TypeError:
            type_error += 1
            count += 1

            continue
        except IndexError:
            index_error += 1
            count += 1

            continue
        i += 1
        count += 1

print(f"type_error:\t{type_error}\tindex_error:\t{index_error}\tcount:\t{count}")
print(f"date:\t{len(date_list)}")
# date_list_res = pd.DataFrame(date_list,index=date_list[:,0])


# second column convert to dateTime and addition in date_list
'''print(f"len:\t{type(res_08_03_1.index[-1][0])}")
date_list1 = []
count_error = 0
# print(f"if_value:\t{res_08_03_1[1].isnull()[25][0]}")
print(f"value:\t{res_08_03_1[1]}\ttype:\t{type(res_08_03_1[1][452][0])}")

for i in range(0, pd.to_numeric(res_08_03_1.index[-1][0])):
    try:
        if res_08_03_1[1].isnull()[i][0] == np.False_:
            date = res_08_03_1[1][i][0]

            if 8 >= len(date) >= 4:

                date = '1/' + date
                date_list1.append(pd.to_datetime(pd.Series(date), format="%d/%m/%Y"))

    except TypeError:
        type_error += 1
        count += 1
        continue

    except IndexError:
        index_error += 1
        count += 1
        continue

    i += 1
    count += 1

print(f"type_error:\t{type_error}\tindex_error:\t{index_error}\tcount:\t{count}")
print(f"date:\t{date_list1}")'''

# third column
date_list2 = []
count_not_null = 0

for i in range(0, pd.to_numeric(res_08_03_1.index[-1][0])):
    try:
        if res_08_03_1[2].isnull()[i][0] == np.False_:
            date = res_08_03_1[2][i][0]

            print(f"null:\t{res_08_03_1[2].isnull()[i][0]}\tindex:\t{i}\ttype:\t{type(date)}\tvalue:\t{date}")
            name_month = re.search(r' \w{3,9} ', date)

            if name_month is not None:
                date = f"{date[:2]}/{define_number_of_month(name_month.group().strip())}/{date[-4:]}"
                print(f"month:\t{name_month.group()}\tvalue:\t{date}")
                date_list2.append(pd.to_datetime(pd.Series(date), format="%d/%m/%Y"))

    except TypeError:
        type_error += 1
        count += 1
        continue

    except IndexError:
        index_error += 1
        count += 1
        continue

    i += 1
    count += 1

# print(f"type_error:\t{type_error}\tindex_error:\t{index_error}\tcount:\t{count}")
# print(f"list+++++++++:\n{date_list2}")
# print(f"list_indexes{list_indexes}")
# print(f"value:{}")
