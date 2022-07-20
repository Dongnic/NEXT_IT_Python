import csv
new_data = []
with open('news.csv', newline='') as f:
    reader = csv.reader(f, delimiter='|', quotechar='')
    for row in reader:
        new_data.append(row)
print(new_data)