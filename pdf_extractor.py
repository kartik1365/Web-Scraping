import csv
import io
all_links = []
with open('Data Engineer Task - Data Engineer Task.csv') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        all_links.append(row[0])

for link in all_links:
    print(link)
