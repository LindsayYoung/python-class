temp = int(raw_input("What is the tempature? "))
humidity =  raw_input("is humidity high or low ")
tornado_warning = raw_input("Do you see a tornado? ")
# elsif example

# I want a special message for extreme conditions
if (temp >= 100) and (humidity == "high"):
	print("Heat advisory due to humidity and high tempature. Use extra caution")
# Want to print this if it is humid. I don't want to print the first if and this statement because that would be repetitive. 
elif (temp > 80) and (humidity == "high"):
	print("Heat advisory due to humidity")
# Want to print this if it is hot but not if it is hot and humid. If it is hot and humid we already gave the "extra caution" message.
elif temp > 100:
	print("Heat advisory due to tempture")
# we checked all the conditions for a heat advisory and none of them applied
else:
	print("No heat advisory")

# If these were all if statements, then on the very hot humid days we would too many repetitive messages.
# Another benefit is that our else statments keeps track of three different ways there could be a heat advisory. 

# this additional contition will always be evaluated, regardless of the previous statement 
if tornado_warning == 'yes':
	print("Stop worring about the heat and take cover!")
