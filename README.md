Python Class
============

Sunlight's 2014 Summer Python class

#Syllabus
* [First class](#first-class): variables, types, list, dictionary
* [Second class](#second-class):  data types, data structures, conditional, user input, command line
* [Third class](#third-class): command line, loops, range
* Fourth class: functions
* Fifth class: CSV reading and writing
* Sixth class: APIs
* Start projects!

[Additional resources](#additional-resources)


***
# First Class!
06/18/2014
[See lesson-1/first_class.py for more notes and code](https://github.com/LindsayYoung/python-class/blob/master/lesson-1/first_class.py)

* Intro

* What is Python?
* A Python program (or any program) is a list of instructions for you computer
* Python is an intermediate language that makes these instructions somewhat more readable for humans
* Like any language, Python has syntax and grammatical rules that you need to follow to facilitate understanding between yourself and the computer
* Breaking these rules causes syntax errors that break your program

* [PythonAnywhere](https://www.pythonanywhere.com)
1. run a line of code directly in the IPython console (we are using 2.7)
2. make a file and click save and run
3. make a file and  and open the Bash console and type: python the_name_of_your_file.py

(You can only have 2 consoles open at a time so you may have to close a console to see the console options)

* The python prompt
* “Hello World!”
* Your first file!
* “Hello World!”
* The Bash prompt

###Variables and assignment
types and changing types - 
* `int()` 
* `str()`
* `float()`

###first data structures
* list
* dictionary

###Homework-
[Homework inspired by Nicko](http://sunlightfoundation.com/blog/2010/12/02/sunlights-political-action-committee-pac-name-generator/)

print a super PAC name using string indices. Here is your list:

```
pac_list = [ "Action", "Against",  "Americans", "Awesome", "Citizens", "Committee", "Communist", "Country", "For", "Freedom", "Liberty", "PAC", "Patriots", "People", "Progressive", "Restore", "Results", "Sunlight", "Super", "Taxpayers", "United", "Values", "Votes", "Zealots", "Zombies"]
```

Extra credit: find the random integer function to create a new name each time you run the program. (Hint: google “python random integer”)

***
# Second Class!
06/18/2014

###Data types
* string - letters or numbers as text
* int - integer number
* float - decimal number
* use `type()` to discover the type of something
* change type with `string()`, `int()`, `float()`
new data type:
* boolean - that is just a fancy way to say things that are `True` or `False`


###Data Structures

###lists
* lists are ordered
* use brackets [ ]
* add to the list with `.append()`
* remove to a list with `.remove()`
* order a list `sorted()`
* splice a list
example:
```
>>> my_list = [4,3,2,6,1,5]
>>> my_list[0]
4
>>> my_list[-1]
5
>>> my_list[2:4]
[2, 6]
>>> sorted(my_list)
[1, 2, 3, 4, 5, 6]
>>> sorted(my_list, reverse=True)
[6, 5, 4, 3, 2, 1]
>>> my_list.append(7)
>>> print(my_list)
[4, 3, 2, 6, 1, 5, 7]
>>> my_list.remove(7)
>>> print(my_list)
[4, 3, 2, 6, 1, 5]
```

###dictionaries
* key value pairs
* use curly braces { } (we decided curly braces look like open dictionary books)
* lookup by key
* the key must be unique
* delete form a dictionary with del
example:
```
>>> my_dictionary = {'DE':'Delaware', 'PA':'Pennsylvania'}
>>> # there is no order in dictionaries, so no sorting
>>> my_dictionary['DE']
'Delaware'
>>> my_dictionary['NJ'] = 'New Jersey'
>>> print(my_dictionary)
{'NJ': 'New Jersey', 'DE': 'Delaware', 'PA': 'Pennsylvania'}
>>> del my_dictionary['NJ']
>>> print(my_dictionary)
{'DE': 'Delaware', 'PA': 'Pennsylvania'}
```
###flow control

###conditional statements
We can check if something is true or false and make our program respond differently 

Here are some helpful operators to make comparisons
* `==` equal
* `!=` not equal
* `>` greater than
* `>=` greater than or equal to
* `<` less than
* `<=` less than or equal to
* `not` means, not

'if'
* `if` is a reserved word in Python that will trigger code to do something only if that condition is met.
* make sure to put a colon after your if statement
* if statements depend on consistent indentation to know what you want
* to check for equality, use == (we use = for assigning a variable)
example:
```
>>> python_class = 'fun'
>>> if python_class == 'lame':
...     print("This class is lame")
... 
>>> if python_class == 'fun':
...	    print("This class is as fun!")
This class is fun!
``` 

'else'
* use else when you have a case not covered by if that you want to behave differently
* remember indention and a colon!

```
>>> python_class = 'fun'
>>> if python_class != 'fun':
...     print("Python class is not fun")
... else:
...     print("I love making computers do my bidding!")
... 
I love making computers do my bidding!
```

'elif'

The world is full of boundless opportunities and we might want to check for many things.
```
if my_bank_account > 1000000000:
	print('retire now')
elif my_bank_account < 1:
	print('look for new job')
else:
	print("keep on truckin'!")
```
Here is another example dedicated to Caitlin 
 
###Take user input
`raw_input()`
We generally make programs and want them to respond to people and the real world. `raw_input()` will take a value from the user that you can use in your program. 
* add directions as a string in the parenthesis so you user knows what to do
```
>>> name = raw_input("what is your name?")
what is your name?Lindsay
>>> response = "Hello, " + name
>>> print response
Hello, Lindsay
```
Ready to make a real program?

Let's look at: 
###[lesson 2 code](https://github.com/LindsayYoung/python-class/blob/master/lesson-2/states.py)

We also covered terminal and file systems because PythonAnywhere was down:
###Command line

(Most of us Mac users used a Bash Terminal)

1) We opened terminal and typed `pwd`, then enter. (`pwd` stands for "print working directory") This printed out where we were in the file system. When we opened our terminal, we were in our home directory. People's home directory can be named anything in this example, my home directory is "home_directory."

2) We saved our file with the name 'states.py' and put it in a new folder called code in our home directory. The '.py' at the end of the file name tells the computer that the file is a python program.
 ```
home_directory
	|
	|-code
		|-states.py
 ```
3) We went back to the terminal and typed `ls`, then enter. (`ls` stands for list) This listed everything in our home directory. We could find the code folder if it was properly saved in the home directory. 

Then, there were two ways of running the program:

1) We could run the program by typing `python code/states.py`, then enter. 'python' tells the terminal to run your program with python. Then, we gave it the location of the file with the folder name, a slash and the filename.

2) We can also move to the folder by typing 'cd code', then enter. (`cd` stands for "change directory" and "code" is the name of our folder) If we type 'ls' enter again, we can see our file `states.py`. Now that we are in the directory of our file, we can run the program by typing `python states.py`, then enter.

Command line is not bad once you get the hang of it, but it takes some practice. 

This is a great resource from the Boston Python Workshop about to use a terminal to run python:
* [for Mac computers](https://openhatch.org/wiki/Boston_Python_Workshop_8/Friday/OSX_Python_scripts)
* [for Windows computers](https://openhatch.org/wiki/Boston_Python_Workshop_8/Friday/Windows_terminal_navigation)
* [for Linux computers](https://openhatch.org/wiki/Boston_Python_Workshop_8/Friday/Linux_Python_scripts)

Here's another resource, [Command Line Crash Corse](http://cli.learncodethehardway.org/book/), that explains command line basics.

***
# Third Class!
07/02/2014
###Command line review

The comand line is a way of operating system without GUI. GUI stands for grapical user interface and it is the point and click way that you are used to using a computer.

When you are in the command line you are always in a place in your file system. To find out where you are you can use, `pwd` to print the current working directory. To see the folders and files directly below where you are you can use `ls` to list the files and folders of your current directory. Use `cd` to change your directory.

To run a python program from command line, change to the directory of the file and type `python name_of_your_file.py`

### Loops

Loops perform a set tasks that you give them over and over. It is extremely useful to write programs to do boring repetitive tasks for you. 

### For loops

"for" is a key word in Python that is used in loops. After 'for' you pass in a variable that you can use on each iteration of the loop. Then, you pass in the object you want to loop through. Like if statements, don't forget the colon and indentation.

Here is an example:
```
>>>shopping_list = ["apple", "orange", "bread", "milk"]
>>>for item in shoping_list:
...  print item
apple
orange
bread
milk
```
That function went through each item in the list and printed it. 

Say you wanted to do some thing a set amount of times. You can use the `range()` function. Range takes an integer and creates a list that is as long as the integer you give it.

Example:
``` 
>>> print range(5)
[0, 1, 2, 3, 4]

```

The following program will print "hello" three times using range.
```
>>>for n in range(3):
...  print("hello")
hello
hello
hello
```
In the previous example we pass in 'n' because we are using it for counting. The variable you pass in can be anything you want. The first time through the loop, n is representing 0, the next time it is representing 1. finally, n represents, 2 the last item in the list provided by the range function. 

Dictionaries can be looped through as well. We will loop through each key in the dictionary using the `.keys()` function.
```
>>> person = {'first_name':'Jane', 'last_name':'Doe'}
>>> for name in person.keys():
...     print name
...     print person[name]
... 
first_name
Jane
last_name
Doe
```
In that example, each loop name is the variable for the dictionary key that is being passed in. For each iteration of the loop when the program gets to `print name` the key is printed then, the next line `print person[name]` also executes because it is at the same indentation. In that line, we look up the value using the key in the dictionary and print the value.

### While loops

'while' is another way to control loops. Instead of doing something a set number of times, the program will keep looping until a condition is met. If the condition is never met, you have made an infinite loop and will need to use 'CTRL-C' to stop the loop.

Don't forget indention and your colon.

```
>>> var = 5
>>> while var < 8:
...     print var
...     var = var + 1
... 
5
6
7
```
We added one to our variable, 'var', and and continued to do so until var was no longer less than 8. 

Lets try making a game based on a while loop. 
* Open a file in your text editor. Let's name it 'gessing_game.py'
* Save that file in your code folder, so we can find it easily later
* We will make something based on [guess_a_number_loop.py](https://github.com/LindsayYoung/python-class/blob/master/lesson-3/guess_a_number_loop.py)

See the code we made during class [here].(https://github.com/LindsayYoung/python-class/blob/master/lesson-3/number_game.py) We also saw that using print statements can help in debugging when there is a logical error or a typo. 

***
# Fourth Class!
07/09/2014
###Functions
Functions are contained, reusable bits of code.

We have been using built-in functions. Here are some useful ones:
```
>>> print("hello")
hello
>>> # len stans for length and gives you the length of an object like a string or list
... len("hello")
5
>>> range(5)
[0, 1, 2, 3, 4]
>>> raw_input("example")
examplehello
'hello'
>>> str(1)
'1'
>>> int('1')
1

```
Now, it is time to build your own function. You probably noticed all of those functions use paresis. We will need paresis to call our function. "Calling a function" just means running the code in that function.

In writing our function we need to use `def` to define it, name our function, have paresis, use a colon and put the code inside
```
def our_function():
	print "hello"

```
We just wrote our first function! But how do we run it? 

We call the function like this:
```
our_function()
``` 



Other concepts we should cover:
* use `in` for a list
* how the script will run in sequence 
* passing a variable into a function
* variable scope



***
#Additional resources

The official Python documentation: 
* [http://docs.python.org/](http://docs.python.org/)

Additional practice:
* [http://www.codecademy.com/](http://www.codecademy.com/)
* [http://learnpythonthehardway.org/book/](http://learnpythonthehardway.org/book/)

Book:
* [Hello World](http://www.barnesandnoble.com/listing/2691811512844?r=1&cm_mmc=GooglePLA-_-Book_25To44-_-Q000000633-_-2691811512844)

Other Resources:

* Beginning guide [https://wiki.python.org/moin/BeginnersGuide/Programmers](https://wiki.python.org/moin/BeginnersGuide/Programmers) 

* A repository with good examples to use as reference[anthonydb/python-get-started](https://github.com/anthonydb/python-get-started)

* A list of reserved words [python.org](https://docs.python.org/release/2.5.4/ref/keywords.html)


