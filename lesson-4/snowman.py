# Make a word guessing game using functions
snow_1 = "      _     "
snow_2 = "    _|=|_   "
snow_3 = "    ('')    "
snow_4 = ">--( o  )--<"
snow_5 = "  ( o    )  "


snow_man = [snow_1, snow_2, snow_3, snow_4, snow_5]

def print_snow(snow_man):
	for snow in snow_man:
		print snow

def print_answer(answer):
	output = ''
	for letter in answer:
		output = output + "_ "
	print output

answer = "python"

correct_guesses = []

while len(answer) != len(correct_guesses):
	print("I am thinking of a word ")
	print_answer(answer)

	guess = raw_input("guess a letter")

	if guess in answer:
		print "You got it"
		correct_guesses.append(guess)
	else:
		print_snow(snow_man)
		snow_man.remove(snow_man[0])
		# or you can use--
		# snow_man.pop(0)
		
