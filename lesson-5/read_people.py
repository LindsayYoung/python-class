# import csv functionality 
import csv

# opening in a way that will close the file when we are done
with open('people.csv', 'rb') as csvfile:
	# reading file
    reader = csv.reader(csvfile)
    # looping through the lines in the csv
    for row in reader:
		print(row)
		print("now print the first three cells")
		print(row[0])
		print(row[1])
		print(row[2])