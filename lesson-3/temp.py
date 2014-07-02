temp = raw_input("What is the tempature? ")
humidity =  raw_input("is humidity high or low ")

# I want a special message for extreme conditions
if temp < 100 and humidity == "high" :
	print "Heat advisory due to humidity and high tempature. Use extra caution"
# Want to print this if it is humid but not if it is hot and humid, because the first line is better for that
elif temp > 80 and humidity == "high":
	print "Heat advisory due to humidity"
# Want to print this if it is hot but not if it is hot and humid, because the first line is better for that
elif temp > 100:
	print "Heat advisory due to tempture"
# we checked all the conditions for a heat advisory and none of them applied
else:
	print "No heat advisory"

