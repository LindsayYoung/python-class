import csv 
# wb for writing
with open("eggs.csv", "wb") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['a1', 'b1', 'c1'])
	writer.writerow(['a2', 'b2', 'c2'])