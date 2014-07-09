# Make a word guessing game using functions

# these are strings that I will put into a list
snow_1 = "      _     "
snow_2 = "    _|=|_   "
snow_3 = "    ('')    "
snow_4 = ">--( o  )--<"
snow_5 = "  ( o    )  "

# this is the list of snow man strings
snow_man = [snow_1, snow_2, snow_3, snow_4, snow_5]

# defining my functions first

# this function takes in the snow_man list
def print_snow(snow_man):
	# looping through each item in the snow_man list 
	for snow in snow_man:
		# printing snow, the item we are looping through
		print snow

# this is the function that prints out the answer in blank line format like: _ _ _ _ _ _ 
# (you will want to modify this function to print letters to replace the blanks as you go)
def print_answer(answer):
	# I am defining the varible output before I start adding to it in my loop
	output = ''
	# looping through each letter in answer
	for letter in answer:
		# Adding a dash and a space to output for each letter
		output = output + "_ "
	# printing output
	print output

# defining variables, They must be defined before we use them later

# here is the answer to our program
answer = "python"

# this is an empty list for guesses
correct_guesses = []

# This is the while loop that will keep going as long as the length of the answer is not equal to the length of correct guesses
while len(answer) != len(correct_guesses):
	# prining banter
	print("I am thinking of a word ")
	# calling the print answer funciton
	print_answer(answer)
	# asking for a letter guess
	guess = raw_input("guess a letter")
	# if the guess is in the answer
	if guess in answer:
		print "You got it"
		# add the answer to the list of correct guesses
		correct_guesses.append(guess)
	# incorrect guess
	else:
		# calling the print_snow function and passing in our snow_man list
		print_snow(snow_man)
		# removing a piece of the snowman by getting rid of the first thing in the list
		snow_man.remove(snow_man[0])
		# or you can use--
		# snow_man.pop(0)
