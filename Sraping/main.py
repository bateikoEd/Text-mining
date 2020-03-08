import pandas as pd

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)

res = df.str.extractall(r'(\d{4})|(\d{1,2}[-./ ]\w+[-./ ]\d{2,4})|(\w+[., -]+\d{2,4}[,. -]+\d{4})|(\w+\s+\w+[,.]\s+\d{4})')
print(res)