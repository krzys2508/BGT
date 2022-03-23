import pandas as pd
import csv

out = pd.read_csv('charts.csv')

# print(out.head(10))


title_frueq = dict()
with open('./charts.csv', encoding="utf8") as out2:
    file = csv.DictReader(out2)
    for lines in file:
        if lines["title"] not in title_frueq:
            title_frueq[lines["title"]] = 1
        else:
            title_frueq[lines["title"]] += 1
    final_frueq = dict(sorted(title_frueq.items(), key=lambda x: x[1]))
    lst = list(final_frueq.items())
    lstreversed = list(reversed(final_frueq.items()))
print(lst[0])
print(lstreversed[0])
#print(list(reversed(final_frueq)[0]))
