# You use import to get additional python functionality that is already installed but not loaded automatically
import random

# create a random integer between 1 and 99
secret = random.randint(1,99)

# creating these variables to keep track of gesses and tries
guess = 0
tries = 0

print("I am a magical leprechaun, to win my pot of gold, guess my number between 1 and 99. You only get 6 guesses.")

while guess != secret and tries <6:
    guess = raw_input("do you know the number?")
    if guess < secret:
        raw_input(str(guess) + "- that's too low!")
    elif guess > secret:
        raw_input(str(guess) + " is too high!")
    tries = tries + 1

if guess == secret:
    print("First they were after my lucky charms, now you get my gold too!")
else:
    print("I am keeping my pot of gold- it is magically delicious")
