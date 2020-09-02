import csv

csvfilepath = "./data.csv"

with open(csvfilepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='-', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['month', 'date', 'year', 'title', 'description', 'imageurl', 'moreinfourl'])
