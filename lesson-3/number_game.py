import random

# create a random integer between 1 and 10
secret = random.randint(1,10)

guess = int(raw_input("Pick a number between 1 and 10!"))
tries = 4

if guess == secret:
	print("WOw YOu are good!")

while guess != secret and tries > 0:
	if guess > secret:
		print("Your guess was too high")
	else:
		print("Your guess was too low")
	guess = raw_input("Pick a number between 1 and 10!")
	guess = int(guess)
	tries = tries - 1



if guess == secret:
	print("You WON!!!")
else:
	print("sorry, try again!")


