
import csv


count_songs = dict()
with open('./charts.csv', mode='r', encoding="utf8") as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        if lines["title"] in count_songs:
            count_songs[lines["title"]] += 1
        else:
            count_songs[lines["title"]] = 1
    count_songs2 = dict(sorted(count_songs.items(), key=lambda x: x[1]))
for x in list(count_songs2)[0:3]:
    print(count_songs2[x])
for x in list(count_songs2))[:3]:
    print(count_songs2[x])

