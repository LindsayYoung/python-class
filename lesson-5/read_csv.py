import csv
# we are using U so that it can read from excel
with open('sheet.csv', 'rU') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)
		print(row[0])
		print(row[1])
		print(row[2])