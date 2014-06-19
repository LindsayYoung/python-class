# I am a comment because there is a hash mark at the beginning of the line, the computer will not read it

#### TYPES

# string
# you can use singe quotes or double quotes to denote a string
# Below you see """Taxp"ayers'""" because it uses 3 double quotes I can put a quote in it
"Happy"

# interger, a non-deimal number
4

# float, a decimal number - use floats for math
3.4

# you can add like types together
example = "the" + "9"

# you cannot add unlike types together
# if you try to run the next line, it will give you an error
# examlple = "the" + 9

##### Variables
# store a value
answer = 3 + 4
# the name on the left remembers what you give it
# don't use spaces, or begin with a number
something_scarry = "vampires"
# here you print the value of the answer
print(answer)
print(something_scarry)

#### Data structures

# This is our list example, remember order matters!
pac_list = [ 'Action', 'Against',  'Americans', 'Awesome',
'Citizens', 'Committee', 'Communist', 'Country', 'For',
'Freedom', 'Liberty', 'PAC', 'Patriots', 'People', 'Progressive',
'Restore',  'Results', 'Sunlight', 'Super', """Taxp"ayers'""", 'United',
'Values', 'Votes', 'Zealots', 'Zombies']

# to access an item in a list, count the items starting with 0
# in the list above, 'Action' is the zeroth item
action = pac_list[0]

# This is concatonation, adding strings together our list item ar all stings so this works
pac = pac_list[24] + " " + pac_list[1] + " " + pac_list[9]

print(pac_list)

# This is how you add to a list
pac_list.append("Freedom Fighters")

print(pac_list)
# now freedom fighters is at the end of the list


# This is an example of a dictionary, it useses key value pairs. The key must be unique
# you can pair a key with a string, list, number, dictionary etc.
random_dictionary = {"Lindsay": ["person", "teacher", 29], "Whinnie": "dog", "Lindsey": "person" }

# this will print the value of "Lindsay" in the random_dictionary dictionary, which is the list ["person", "teacher", 29]
print(random_dictionary["Lindsay"])

# this will print the value of "Whinnie" witch is "dog"
print(random_dictionary["Whinnie"])

print(random_dictionary)

# this is how you add to a dictionary
random_dictionary["Lassie"] = "dog"
print(random_dictionary)
